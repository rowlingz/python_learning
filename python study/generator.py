# 生成器

# 生成器表达式
l1 = [i for i in range(5)]      # [] 返回列表
l2 = (i for i in range(5))      # （）返回生成器表达式
print(l1)
print(l2)


# 生成器通过生成器函数定义，采用yield一次返回一个值
def Zrange(n):
    i = 0
    while i < n:
        yield i
        i += 1


zrange = Zrange(2)
print(zrange.__next__())


g = (i for i in range(50) if i % 2 == 0)
print([i for i in g])


# 递归生成器--全排列
def permutations(s):
    if len(s) == 0:
        yield s
    else:
        for i in range(len(s)):
            s[0], s[i] = s[i], s[0]
            for j in permutations(s[1:]):
                yield [s[0]] + j


s = [32, 32, 78]
li = [i for i in permutations(s)]
print(li)




