import numpy as np
import pandas as pd
from scipy import stats
import timeit


def fill_fre_top_5(x):
    if len(x) <= 5:
        new_array = np.full(5, np.nan)
        new_array[0: len(x)] = x
        return new_array


def data_analysis(miss_set = [np.nan, 9999999999, -999999], data=None):
    # 1.count
    count = data.apply(lambda x: len(x.unique()))
    count = count.to_frame('count')

    # 2.count zero
    count_zero = data.apply(lambda x: np.sum(x == 0))
    count_zero = count_zero.to_frame('count_zero')

    # 3.Mean
    data_mean = data.apply(lambda x: np.mean(x[~np.isin(x, miss_set)]))
    data_mean = data_mean.to_frame('data_mean')

    # Median
    data_median = data.apply(lambda x: np.median(x[~np.isin(x, miss_set)]))
    data_median= data_median.to_frame('data_median')

    # Mode
    data_mode = data.apply(lambda x: stats.mode(x[~np.isin(x, miss_set)])[0][0])
    data_mode = data_mode.to_frame('data_mode')

    # Mode percentage
    data_mode_count = data.apply(lambda x: stats.mode(x[~np.isin(x, miss_set)])[1][0])
    data_mode_count = data_mode_count.to_frame('data_mode_count')
    data_mode_perct = data_mode_count / data.shape[0]
    data_mode_perct.columns = ['data_mode_perct']

    # max
    data_max = data.apply(lambda x: np.max(x[~np.isin(x, miss_set)]))
    data_max = data_max.to_frame('data_max')

    # quantile
    json_fre_name = {}
    json_fre_count = {}
    for i, name in enumerate(data.columns):
        index_name = data[name][~np.isin(data[name], miss_set)].value_counts().iloc[0:5, ].index.values
        index_name = fill_fre_top_5(index_name)
        json_fre_name[name] = index_name

        value_count = data[name][~np.isin(data[name], miss_set)].value_counts().iloc[0:5, ].index.values
        value_count = fill_fre_top_5(value_count)
        json_fre_count[name] =  value_count

    data_fre_name = pd.DataFrame(json_fre_name)[data.columns].T
    data_fre_count = pd.DataFrame(json_fre_count)[data.columns].T
    data_fre = pd.concat([data_fre_name, data_fre_count], axis=1)
    # data_fre.columns = data.columns

    # Miss value count
    data_miss = data.apply(lambda x: np.sum(x[np.isin(x, miss_set)]))
    data_miss = data_miss.to_frame('freq_miss')

    data_summary = pd.concat(
        [count, count_zero, data_mean, data_median, data_mode,
         data_max, data_fre, data_miss], axis=1
    )

    return data_summary


file_name = "C:\python_project\winequality-red.csv"
data = pd.read_csv(file_name, sep=';')

print(data_analysis(miss_set = [np.nan, 9999999999, -999999], data=data))


