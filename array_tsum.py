# -*- coding:utf-8 -*-
# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。


class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array) == 0:
            return []
        # 递增数组，首次满足条件的对应积就最小，跳出遍历，如果遍历结束，则不存在满足条件的两个数，返回[]
        for i in array:
            dif = tsum - i
            if (dif in array) and (dif > i):
                return [i, dif]
        return []

        # 利用字典存储积，判断最小积
        # out_dic = {}
        # # 字典——存储满足和为tsum的两个数字，key为积，value为两个数字组成的列表
        # for i in array:
        #     dif = tsum - i
        #     if dif in array and dif > i:
        #         mul = i * dif
        #         out_dic[mul] = [i, dif]
        #
        # if len(out_dic) == 0:
        #     return []
        # for key in sorted(out_dic.keys()):
        #     # 只返回积最小的value
        #     return out_dic[key]


array = []
tsum = 0
t = Solution()
s = t.FindNumbersWithSum(array,tsum)
print(s)