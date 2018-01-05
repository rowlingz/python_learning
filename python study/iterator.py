# 迭代器

# 使用iter()函数获取迭代器对象

li = [1, 2, 3, 4]
li = iter(li)
try:
    while True:
        print(li.__iter__())    # 返回迭代器本身
        print(li.__next__())    # 容器中的下一个元素
except StopIteration:
    pass


# 自定义迭代器类
class Myrange():
    """自定义迭代器类Myrang"""
    def __init__(self, n):
        self.num = n
        self.id = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.id < self.num:
            val = self.id
            self.id += 1
            return val
        else:
            raise StopIteration


s = Myrange(3)
for i in s:
    print(i)


# 利用迭代器实现斐波那契数列
class Fib():
    """利用迭代器实现斐波那契数列(可迭代对象)"""
    def __init__(self, n):
        self.n = n
        self.id, self.a, self.b = 0, 0, 1

    def __next__(self):
        if self.id < self.n:
            result = self.b
            self.a, self.b = self.b, self.a + self.b
            self.id += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        return self


f = Fib(5)
for i in f:
    print(i)


