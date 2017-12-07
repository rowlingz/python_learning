# -*- coding:utf-8 -*-
# 对于一个给定的字符序列S，请你把其循环左移K位后的序列输出

class Solution:
    def LeftRotateString(self, s, n):
        if len(s) == n or len(s) == 0:
            return s
        left_string = s[:n]
        return s[n:] + left_string



s = ''
t = Solution()
print(s[4:])
