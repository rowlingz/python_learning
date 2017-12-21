# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# 例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
#  -*- coding:utf-8 -*-


class Solution:
    def PrintMinNumber(self, numbers):
        if numbers is None or len(numbers) == 0:
            return ""
        if len(numbers) == 1:
            return numbers[0]
        output_str = ""
        n = len(numbers)
        # 对数组进行排序
        for i in range(n-1):
            for j in range(i + 1, n):
                if self.max_str(numbers[i], numbers[j]):
                    numbers[i], numbers[j] = numbers[j], numbers[i]

        for number in numbers:
            output_str += str(number)
        return int(output_str)

    def max_str(self, number1, number2):
        n1 = int(str(number1) + str(number2))
        n2 = int(str(number2) + str(number1))
        if n1 > n2:
            return True
        else:
            return False


s = Solution()
numbers = [3,32,321]
print(s.PrintMinNumber(numbers))