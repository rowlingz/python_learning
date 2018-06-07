# -*- coding:utf-8 -*-
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns


def filter_data(str):
    result = re.findall(r'\d+\.?\d*', str)
    if result:
        num = float(result[0])
        if num < 10:
            num = num * 100
    else:
        num = 0

    return num


def gender_height_ana(data):
    data_male = data[data['gender'] == '男']
    data_female = data[data['gender'] == '女']

    hmean_male = data_male['height_num'].mean()
    hmean_female = data_female['height_num'].mean()
    # print(data_male)

    sns.set_style("ticks")

    plt.figure(figsize=(8, 4))

    # 分布密度图（含密度曲线）
    sns.distplot(data_female['height_num'], hist=False, kde=True, rug=True,
                 rug_kws={'color': 'g', 'lw': 2, 'alpha': 0.5, 'height': 0.1},      # 设置数据频率分布颜色
                 kde_kws={'color': 'g', 'lw': 1.5, 'linestyle': '--'},              # 设置密度曲线颜色，线宽，标注、线形
                 label='female_height')

    sns.distplot(data_male['height_num'], hist=False, kde=True, rug=True,
                 rug_kws={'color': 'y', 'lw': 2, 'alpha': 0.5, 'height': 0.1},
                 kde_kws={'color': 'y', 'lw': 1.5, 'linestyle': '--'},
                 label='male_height')

    # 平均身高辅助线，及标注
    plt.axvline(hmean_male, color='y', linestyle=':', alpha=0.8)
    plt.text(hmean_male+2, 0.005, 'male_height_mean: %.f' % hmean_male, color='y')

    plt.axvline(hmean_female, color='y', linestyle=':', alpha=0.8)
    plt.text(hmean_female+2, 0.008, 'female_height_mean: %.f' % hmean_female, color='g')

    # 增加网格线
    plt.grid(linestyle='--')
    plt.title("Athlete's height")
    plt.show()


def bmi_ana(data):
    event_count = data['event'].value_counts()
    event_drop = event_count[event_count > 10]
    data_drop = data[data.event.isin(list(event_drop.index))]

    data_drop['BMI'] = data_drop['weight_num']/(data_drop['height_num']/100)**2
    data_drop['BMI_range'] = pd.cut(data_drop['BMI'], [0, 18.5, 24, 28, 50],
                                    labels=['thin', 'normal', 'strong', 'extremely_strong'])
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(8, 4))

    # 绘制小提琴图
    sns.violinplot(x='event', y='BMI', data=data_drop,
                   scale='count',
                   palette="hls",  # 设置调色盘
                   inner="quartile")

    # 绘制内部散点图
    sns.swarmplot(x='event', y='BMI', data=data_drop, color='w', alpha=0.8, s=2)

    plt.grid(linestyle='--')
    plt.title("Athlete's BMI")

    plt.show()


if __name__ == "__main__":
    df = pd.read_csv(open('运动员信息采集.csv', encoding='utf_8_sig'))
    # print(df)

    data = df[['name', 'gender', 'event', 'height', 'weight']]
    data = data.dropna()

    data['height_num'] = data['height'].apply(filter_data)
    data['weight_num'] = data['weight'].apply(filter_data)
    bmi_ana(data)

