# 操作给定的二叉树，将其变换为源二叉树的镜像

# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, val= None, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        if root.left is not None:
            self.Mirror(root.left)
        if root.right is not None:
            self.Mirror(root.right)


if __name__ == '__main__':
    s = Solution()

    root1 = TreeNode(8, TreeNode(8, TreeNode(9), TreeNode(2, TreeNode(4), TreeNode(7))), TreeNode(7))
    # root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(8, TreeNode(9), TreeNode(4))
    s.Mirror(root1)
