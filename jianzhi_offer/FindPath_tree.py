# -*- coding:utf-8 -*-
# 输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

class TreeNode:
    def __init__(self, val= None, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        pass

    def get_path(self, root):
        # 定义递归中的全局变量，
        path = ''       # 路径
        values = []     # 路径的val数组
        result = []     # 所有路径汇总

        self.helper(root, path, result, values)
        return result

    def helper(self, root, path, result, values):
        if root is None:
            return
        path = path + str(root.val)
        total = values[:]       # 避免更新上级数组，采用切片复制数组
        total.append(root.val)

        if root.left is not None:
            self.helper(root.left, path + '->', result, total)
        if root.right is not None:
            self.helper(root.right, path + '->', result, total)

        if root.left is None and root.right is None:
            result.append(path)
            result.append(total)


class Solution2:
    def FindPath(self, root, expectNumber):
        paths = self.get_path(root)
        summary = []
        for i in paths:
            if sum(i) == expectNumber:
                summary.append(i)

        return summary

    def get_path(self, root):
        values = []
        result = []

        self.helper(root, result, values)
        return result

    def helper(self, root, result, values):
        if root is None:
            return
        total = values[:]
        total.append(root.val)

        if root.left is not None:
            self.helper(root.left, result, total)
        if root.right is not None:
            self.helper(root.right, result, total)

        if root.left is None and root.right is None:
            result.append(total)


if __name__ == '__main__':
    s = Solution2()

    root1 = TreeNode(8, TreeNode(8, TreeNode(9), TreeNode(2, TreeNode(4), TreeNode(7))), TreeNode(7))
    # root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(8, TreeNode(9), TreeNode(4))

    print(s.get_path(root2))
    print(s.get_path(root1))
    print(s.FindPath(root1, 25))
    print(7 % 1000000007)