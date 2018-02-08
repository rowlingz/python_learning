# 数据流中的中位数


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stream = []
        self.count = 0

    def Insert(self, num):
        self.count += 1
        self.stream.append(num)

    def GetMedian(self):
        lis = self.stream[:]
        lis.sort()
        if self.count % 2 == 0:
            mid = self.count / 2
            return (lis[mid] + lis[mid - 1]) / 2
        else:
            mid = self.count // 2
            return lis[mid]



if __name__ == "__main__":
    print(5 // 2)
    a = [4,6,1,2]
    a.sort()
    print(a)
