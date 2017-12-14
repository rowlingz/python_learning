# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here






    def get_kind(self,ss):
        if ss is None:
            return
        new_ss = ""
        for s in ss:
            if s not in new_ss:
                new_ss += s

        return len(new_ss)




ss = 'wsdHbl'
s = ''
print(len(s))