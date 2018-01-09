# Hanoi Tower 汉诺塔问题
# 把A柱子上若干个圆盘（从大到小依次往上），借助柱子B，移动到柱子C上去，要求一次只能移动一个圆盘，且大盘子不能放在小盘子上面
# 递归解题思路：假设已知将n-1个原盘由一个柱子移动到另一个柱子的方法，则当圆盘个数是n个时，将n-1个由A-C，剩余将最大的A-B，
# 最后将C上的n-1移至B


def hanoi(n, a, b, c):
    if n == 1:
        print('move', a, '--->', c)
    else:
        hanoi(n-1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n-1, b, a, c)


print(hanoi(1, 'a', 'b', 'c'))
print(hanoi(3, 'a', 'b', 'c'))


