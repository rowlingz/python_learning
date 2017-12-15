# -*- coding:utf-8 -*-
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。


class Solution:
    def NumberOf1(self, n):
        if n == 0:
            return 0
        bin_number = self.get_bin(n)
        count = 0
        for i in bin_number:
            if i == '1':
                count += 1
        if n > 0:
            return count
        if n < 0:
            count = ((32 - count) + 1) % 32
            return count

    def get_bin(self, n):
        s = ""
        n = abs(n)
        while n != 0:
            s = str(n % 2) + s
            n = n // 2
        return s


s = Solution()
print(s.get_bin(1))
print(s.NumberOf1(-1))