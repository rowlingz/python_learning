# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        number_str = "1234567890"
        symboy = ["+","-"]
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            if s in number_str:
                return int(s)
            else:
                return 0
        for i in range(1, n):
            if s[i] not in number_str:
                return 0
        if s[0] == symboy[0]:
            return int(s[1:])
        if s[0] == symboy[1] or s[0] in number_str:
            return int(s)
        return 0


# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        try:
            number = int(s)
            return number
        except ValueError:
            return 0


