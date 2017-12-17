# -*- coding:utf-8 -*-
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
# 思路：正数只需计算二进制中1的个数，负数的二进制补码形式是正数二进制的反码加1，
# 反码中1的个数为32-count,反码需末端加1，则末端连续个1会转化为1个1，即正数中末端0的个数，
# 所以负数中1的个数32-count-end0+1


class Solution:
    def NumberOf1(self, n):
        if n == 0:
            return 0
        bin_number = self.get_bin(n)
        count = 0
        ends0 = 0
        # end0用来计量二进制中末尾连续0的个数
        for i in bin_number:
            if i == '0':
                ends0 += 1
            else:
                break
        for i in bin_number:
            if i == '1':
                count += 1
        if n > 0:
            return count
        if n < 0:
            count = 32 - count - ends0 + 1
            return count

    def get_bin(self, n):
        """得到非零正整数的倒序二进制字符串"""
        s = ""
        n = abs(n)
        while n != 0:
            s = s + str(n % 2)
            n = n // 2
        return s


s = Solution()
print(s.get_bin(-4))
print(s.NumberOf1(-4))