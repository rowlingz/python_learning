# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba


class Solution:
    def Permutation(self, ss):
        li = list(ss)
        if len(li) < 1:
            yield ss
        else:
            for i in range(len(li)):
                li[0], li[i] = li[i], li[0]
                for j in self.Permutation(li[1:]):
                    yield str(li[0]) + str(j)

s = Solution()
ss = 'aac'
print([i for i in s.Permutation(ss)])