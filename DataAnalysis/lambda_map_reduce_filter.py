# -*- coding: utf-8 -*-
from functools import reduce


"""函数式编程包含函数：lambda/map/reduce/filter"""
# 1 lambda 函数
int1 = [3, 5, 7, 8, 1]
fu = lambda x: x + 2
print([fu(i) for i in int1])


g = lambda x, y: x + y
print(g(1, 3))


a = list('aba34')
print(a.count('a'))
print(tuple('234'))
print(a.index('b'))


print(dict([['a', 1], ['b', 2]]))


# 2 map函数----实现逐一遍历，效率优于列表解析,for循环
a1 = [1, 2, 3]
a2 = [2, 3, 4]
b = map(lambda x, y: x + y, a1, a2)
b = list(b)
print(b)

# 3 reduce函数----用于递归运算
re = reduce(lambda x, y: x*y, range(1, 4))
print(re)

# 4 filter函数---过滤器，需要一个返回值为bool型的函数，筛选出符合条件的值
fi = filter(lambda x: x > 5 and x < 10, range(12))
print(list(fi))
