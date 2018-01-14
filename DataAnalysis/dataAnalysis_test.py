import numpy as np
import matplotlib.pyplot as plt

lis = [[1,3,5], [2,5,7]]
print(type(lis))
np_li = np.array(lis)
print(type(np_li))

# dtype指定数据类型
np_li2 = np.array(lis, dtype=np.float)
print(type(np_li2))

print(np_li2.shape)     # 形状
print(np_li2.ndim)      # 维度
print(np_li2.dtype)     # 类型
print(np_li2.itemsize)  # 每个元素的大小
print(np_li2.size)      # 元素个数

# 特殊数组
print(np.zeros((2, 4)))
print(np.ones((3,)))
# 随机数
print("Rand: ")
print(np.random.rand(3, 2))     # 0~1之间的均匀分布
print(np.random.rand())

print("RandInt: ")
print(np.random.randint(4, 10, (2,2)))      # 随机整数

print("Randn: ")
print(np.random.randn(2, 3))        # 随机正态

print("Choice: ")
print(np.random.choice([1,4,6]))    # 随机选择

print("Distribute: ")
print(np.random.beta(1, 10, (3, 4)))    # 函数分布

print(np.arange(1, 10).reshape([3,3]))

print(np.eye(2))


x = np.linspace(-np.pi, np.pi, 258)
c, s = np.cos(x), np.sin(x)
plt.figure(1)
plt.plot(x, c, label="cos")
plt.plot(x, s)
plt.legend(loc="upper right")
plt.show()