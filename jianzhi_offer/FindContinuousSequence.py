# 输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序


# -*- coding:utf-8 -*-


class Solution:
    def FindContinuousSequence(self, tsum):
        mid = tsum // 2
        begin = 1
        end = 2
        sumlist = []
        cur = begin + end
        while begin <= mid and end < tsum:
            cur = sum(range(begin, end + 1))
            if cur < tsum:
                end += 1
            elif cur == tsum:
                sumlist.append(list(range(begin, end + 1)))
                end += 1
                begin += 2
            elif cur > tsum:
                begin += 1

        return sumlist


s = Solution()
print(s.FindContinuousSequence(100))
