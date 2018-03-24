# -*- coding:utf-8 -*-
# 美国大选资助信息分析
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename = "./pydata-book-master/ch09/P00000001-ALL.csv"

# 1.获取数据
data = pd.read_csv(filename, low_memory=False)


# 候选人党派信息
def get_party(data):
    parties = {'Bachmann, Michelle': 'Republican',
               'Romney, Mitt': 'Republican',
               'Obama, Barack': 'Democrat',
               "Roemer, Charles E. 'Buddy' III": 'Republican',
               'Pawlenty, Timothy': 'Republican',
               'Johnson, Gary Earl': 'Republican',
               'Paul, Ron': 'Republican',
               'Santorum, Rick': 'Republican',
               'Cain, Herman': 'Republican',
               'Gingrich, Newt': 'Republican',
               'McCotter, Thaddeus G': 'Republican',
               'Huntsman, Jon': 'Republican',
               'Perry, Rick': 'Republican'}
    data['party'] = data['cand_nm'].map(parties)
    return data


# 根据职业和雇主统计资助信息
def get_fund(data):

    # 排除负的出资额（退款）
    data = data[data['contb_receipt_amt'] > 0]

    # 职位信息映射
    occ_mapping = {
        'INFORMATION REQUESTED PER BEST EFFORTS': 'NOT PROVIDED',
        'INFORMATION REQUESTED': 'NOT PROVIDED',
        'INFORMATION REQUESTED (BEST EFFORTS)': 'NOT PROVIDED',
        'C.E.O': 'CEO'
    }
    f = lambda x: occ_mapping.get(x, x)
    data.contbr_occupation = data.contbr_occupation.map(f)

    # 雇主信息映射
    emp_mapping = {
        'INFORMATION REQUESTED PER BEST EFFORTS': 'NOT PROVIDED',
        'INFORMATION REQUESTED': 'NOT PROVIDED',
        'SELF': 'SELF-EMPLOYED'
    }
    data.contbr_employer = data.contbr_employer.map(lambda x: emp_mapping.get(x, x))

    # 根据党派和职业对数据聚合
    by_occupation = data.pivot_table('contb_receipt_amt', index='contbr_occupation', columns='party', aggfunc='sum')

    # 滤除总资额不足200万美元的数据
    over_2mm = by_occupation[by_occupation.sum(1) > 2000000]

    # 绘制  各企业对各党派总出资额
    plt.figure()
    over_2mm.plot(kind='barh')
    plt.show()

    return over_2mm


# 了解对两位候选人总出资额最高的职业和企业

def get_top_amounts(group, key, n=5):
    totals = group.groupby(key)['contb_receipt_amt'].sum()
    return totals.sort_values()[-n:]


data_mrbo = data[data.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])]
grouped = data_mrbo.groupby('cand_nm')

high_emp = grouped.apply(get_top_amounts, 'contbr_employer', n=7)
high_occ = grouped.apply(get_top_amounts, 'contbr_occupation', n=10)


# 按出资额的大小将其离散化
bins = np.array([0, 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000])
cats = pd.cut(data_mrbo.contb_receipt_amt, bins)
grouped_cut = data_mrbo.groupby(['cand_nm', cats])
# 资助量
accounts = grouped_cut.size().unstack(0)

# 资助额
accounts_sum = grouped_cut.contb_receipt_amt.sum().unstack(0)

# 赞助额所占比
normed_sum = accounts_sum.div(accounts_sum.sum(axis=1), axis=0)

plt.figure()
normed_sum[:-2].plot(kind='barh', stacked=True)
plt.show()


if __name__ == '__main__':
    data = get_party(data)
    print(normed_sum)
    # print(high_occ)
    # print(get_fund(data))