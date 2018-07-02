# -*- coding: utf-8 -*-

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np


# filename = './data_7/air_data.csv'
# air_data = pd.read_csv(filename, encoding='utf-8')


def get_data(air_data):
    """获取数据，初步获得探索结果"""
    # 获取原始数据
    explore = air_data.describe(percentiles=[], include='all').T

    # 获取缺失值
    explore['null'] = len(air_data) - explore['count']

    # 抽取null max min 生成新的对象
    result = explore[['null', 'min', 'max']]
    # result.columns = ['null', 'min', 'max']

    # 将得到的探索结果result写入文件
    result.to_csv('./data_7/explore.csv', sep=',', header=True)

    print(result)


def data_cleaning(air_data):
    """数据清洗，滤除不合规则的数据"""
    # 舍去票价为空的行
    data = air_data[air_data['SUM_YR_1'].notnull() & air_data['SUM_YR_2'].notnull()]

    # 滤去票价为0， 平均折扣率不为0，总飞行公里数大于0的记录
    index1 = data['SUM_YR_1'] != 0
    index2 = data['SUM_YR_2'] != 0
    index3 = (data['avg_discount'] == 0) & (data['SEG_KM_SUM'] == 0)

    data = data[index1 | index2 | index3]

    data.to_csv('./data/clean_file.csv', sep=',')


def regulation(clean_file):
    """抽取相关属性，对其正则化"""
    data = pd.read_csv(clean_file, sep=',', encoding='utf-8')
    data['L'] = pd.to_datetime(data['LOAD_TIME'], format='%Y/%m/%d') - \
                pd.to_datetime(data['FFP_DATE'], format='%Y/%m/%d')
    data['L'] = data['L'].apply(lambda x: x.days)
    data = data[['L', 'LAST_TO_END', 'FLIGHT_COUNT', 'SEG_KM_SUM', 'avg_discount']]
    data.columns = ['L', 'R', 'F', 'M', 'C']

    # 标准化处理
    data = (data - data.mean()) / (data.std())
    data.to_csv('./data/regulation_file.csv', sep=',')


def dist_euc(vec_a, vec_b):
    """
    两个向量间的欧式距离
    :param vec_a:
    :param vec_b:
    :return:
    """
    dist = np.linalg.norm(vec_a - vec_b)
    return dist


def select_k_value(file):
    """
    尝试不同的K值，用欧式距离评价
    :param file:
    :return:
    """
    data = pd.read_csv(file, sep=',', encoding='utf-8')
    data = np.array(data).astype('float32')
    nums = range(2, 10)
    sse_list = []
    for num in nums:
        sse = 0
        kmodel = KMeans(n_clusters=num, n_jobs=4)
        kmodel.fit(data)

        cluster_center_list = kmodel.cluster_centers_
        cluster_list = kmodel.labels_.tolist()
        for i in range(len(data)):
            cluster_num = cluster_list[i]
            sse += dist_euc(data[i, :], cluster_center_list[cluster_num])
        print('簇是：', num, '时，SSE是：', sse)
        sse_list.append(sse)

    plt.plot(nums, sse_list)
    plt.xlabel('n_clusters')
    plt.ylabel('SSE')
    plt.show()

    # return nums, sse_list


def mode_k_means(file, k=5):
    """模型分析"""
    data = pd.read_csv(file, sep=',', encoding='utf-8')

    # 调用k-means 进行聚类分析
    kmodel = KMeans(n_clusters=k, n_jobs=4)
    kmodel.fit(data)

    # kmodel.cluster_centers_   聚类中心
    df = pd.DataFrame(kmodel.cluster_centers_,
                      columns=['counts', 'L', 'R', 'F', 'M', 'C'],
                      index=['customer' + str(i) for i in range(5)])
    df.to_csv('./data/cluster_center.csv', sep=',')
    print(df)

    # kmodel.labels_   各样本对象类别
    data['result'] = kmodel.labels_
    # print(kmodel.labels_)
    data.to_csv('./data/result.csv', sep=',')


def result_pic(result):
    """雷达图的绘制"""
    result = pd.concat([result, result[['L']]], axis=1)
    kinds = list(result.iloc[:, 0])
    centers = np.array(result.iloc[:, 2:])
    labels = ['L', 'R', 'F', 'M', 'C']

    angle = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    angle = np.concatenate((angle, [angle[0]]))

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)

    for i in range(len(kinds)):
        ax.plot(angle, centers[i], linewidth=2, label=kinds[i])

    ax.set_thetagrids(angle * 180 / np.pi, labels)
    plt.title('different kind')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # regulation('./data/zscoredata.xls')
    # regulation('./data/clean_file.csv')
    # mode_k_means('./data/regulation_file.csv')
    # print('end')
    result = pd.read_csv('./data_7/cluster_center.csv', sep=',')
    # result_pic(result)
    select_k_value('./data_7/regulation_file.csv')
    print('end')
