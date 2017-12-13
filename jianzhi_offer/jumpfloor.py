# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
# 只有一步时，只有1种跳法；有两步时，就有2中跳法了.
# 当布数大于2部后，可以选择跳一步或两部，则有f(n) = f(n-1) + f(n-2)

class Solution:
    def jumpFloor_1(self, number):
        # 递归算法
        if number == 1:
            return 1
        if number == 2:
            return 2
        return self.jumpFloor_1(number - 1) + self.jumpFloor_1(number - 2)

    def jumpFloor_2(self, number):
        # 迭代
        if number == 1:
            return 1
        elif number == 2:
            return 2
        elif number > 2:
            f_1, f_2 = 1, 2
            for i in range(3, number + 1):
                f_1, f_2 = f_2, f_1 + f_2
            return f_2

    def jumpFloorII(self, number):
        # 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
        # f(n) = f(n-1) + f(n-2) +  ··· + f(1) + f(0)
        # f(n-1) = f(n-2) +  ··· + f(1) + f(0)
        # ····
        # f(2) = f(1) + f(0)
        # f(1) = 1, f(0) =1
        # 得到
        # f(n) = 2f(n-1)
        # ····
        # f(2) = 2f(1)

        f = 1
        while number != 1:
            f = 2 * f
            number -= 1
        return f

    def rectCover(self, number):
        if number == 1:
            return 1
        if number == 2:
            return 2
        if number > 2:
            f_1, f_2 = 1, 2
            for i in range(3,number + 1):
                f_1


s = Solution()
print(s.jumpFloor_1(5))
print(s.jumpFloor_2(5))
print(s.jumpFloorII(2))
