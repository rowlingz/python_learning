# -*- coding:utf-8 -*-
# 翻转字符串中单词顺序


class Solution:
    def ReverseSentence(self, s):
        if len(s) == 0:
            return s
        list_s = s.split()
        rever_s = ""
        if len(list_s) <= 1:
            return s
        while len(list_s) > 1:
            word = list_s.pop()
            rever_s = rever_s + word + " "
        return rever_s + list_s[0]






s = "  "
print(len(s.split()))
t = Solution()
print(t.ReverseSentence(s))