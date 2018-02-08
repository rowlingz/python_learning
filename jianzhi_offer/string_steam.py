# 找出字符流中第一个只出现一次的字符。
# 例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
# 当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。


# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        # 用两个数组存储字符流中的字符
        self.repeat_appear = []
        self.once_appear = []

    def FirstAppearingOnce(self):
        # self.once_appear依次存储了只出现一次的字符，则返回self.once_appear[0]，或为'#'
        if self.once_appear == []:
            return '#'
        else:
            return self.once_appear[0]

    def Insert(self, char):
        # 如果出现的字符从未出现过，加载在self.once_appear
        if char not in self.once_appear:
            if char not in self.repeat_appear:
                self.once_appear.append(char)
        # 出现的字符在self.once_appear中，将其加载到self.repeat_appear中，并从self.once_appear删除。
        else:
            self.repeat_appear.append(char)
            self.once_appear.remove(char)

