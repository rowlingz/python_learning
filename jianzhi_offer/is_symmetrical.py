# 判断二叉树是否对称

# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, val= None, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot is None:
            return True

        return self.issame(pRoot.left, pRoot.right)

    def issame(self, p1, p2):
        if not p1 and not p2:
            return True
        if p1 and p2:
            if p1.val != p2.val:
                return False
            else:
                return self.issame(p1.left, p2.right) and self.issame(p1.right, p2.left)

        return False


if __name__ == '__main__':
    s = Solution()

    root1 = TreeNode(8, TreeNode(8, TreeNode(9), TreeNode(2, TreeNode(4), TreeNode(7))), TreeNode(7))
    # root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(8, TreeNode(9), TreeNode(9))
    print(s.isSymmetrical(root2))