# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba


# class Solution:
#     def Permutation(self, ss):
#         li = list(ss)
#         if len(li) < 1:
#             yield ss
#         else:
#             for i in range(len(li)):
#                 li[0], li[i] = li[i], li[0]
#                 for j in self.Permutation(''.join(li[1:])):
#                     yield str(li[0]) + str(j)
#
# s = Solution()
# ss = 'aac'
# print([i for i in s.Permutation(ss)])
#
# tem = "abc"
# print(set([i for i in s.Permutation(ss)]))


class Solution:
    # 借助递归生成器生成全排列列表组合
    def iter_list(self, str_to_list):
        if len(str_to_list) == 0:
            yield str_to_list
        else:
            for i in range(len(str_to_list)):
                str_to_list[0], str_to_list[i] = str_to_list[i], str_to_list[0]
                for j in self.iter_list(str_to_list[1:]):
                    yield [str_to_list[0]] + j

    def Permutation(self, ss):
        if len(ss) <= 1:
            return ss
        _to_list = list(ss)
        result_list = []
        for i in self.iter_list(_to_list):
            word = ''.join(i)
            if word not in result_list:
                result_list.append(word)
        return self.sorted_list(result_list)

    def sorted_word(self, a, b):
        n = len(a)
        for i in range(n):
            asc_a, asc_b = ord(a[i]), ord(b[i])
            if asc_a == asc_b:
                continue
            elif asc_a > asc_b:
                return True
            else:
                return False

    def sorted_list(self, str_list):
        n = len(str_list)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.sorted_word(str_list[i], str_list[j]):
                    str_list[i], str_list[j] = str_list[j], str_list[i]

        return str_list

s = Solution()
ss = 'abc'
print(s.Permutation(ss))

