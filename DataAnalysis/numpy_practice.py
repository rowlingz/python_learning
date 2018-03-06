# -*- coding:utf-8 -*-
import numpy as np

lis = [[1, 2, 3], [5, 6, 7]]
# np.array() 数组转换为ndarray
np_lis = np.array(lis)


def use_numpy():

    # dtype 返回数据类型
    print(np_lis.dtype)

    # shape 返回数组维度
    print(np_lis.shape)


    # zeros 和 ones创建指定长度或形状的全0或全1数组
    print(np.zeros((3, 6), dtype=np.float))
    print(np.ones(8))

    # 返回range(8)数组
    print(np.arange(8))

    arr = np.array([1.2, 3.4, 7.6])
    print(arr.dtype)
    # astype函数转换数组类型为指定类型
    arr1 = arr.astype(np.int32)
    print(arr1.dtype)


def np_where(array):
    """where函数依照特定条件创建新的数组"""
    print(np.where(array > 0, 2, -2))


def np_where1(array, condition1, condition2):
    """利用嵌套where创建复杂逻辑"""
    print(np.where(condition1 & condition2, 0,
                   np.where(condition1, 1,
                            np.where(condition2, 2, 3))))
    """ 等价于
    if condition1 and condition2:
        return 0
    elif condition1:
        return 1
    elif condition2:
        return 2
    else:
        return 3
    """


if __name__ == "__main__":
    print(np_lis * 10)
    print(np_lis + np_lis)
    arr = np.array([1.2, 3.4, 7.6])
    print(arr.dtype)
    arr1 = arr.astype(np.int32)
    print(arr1.dtype)
    arr = np.random.randn(4, 3)
    print(arr)
    np_where(arr)

    np_where1(arr, arr > 0, arr < 0.5)

    print(arr.mean())
    print(arr.mean(axis=1))
    print(arr.mean(0))
    print(arr.sum())
    print((arr > 0).sum())

    print(np.random.randint())



