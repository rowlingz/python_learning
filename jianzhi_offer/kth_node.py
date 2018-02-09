# 搜索二叉搜索树的第K大结点。

# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, val= None, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def KthNode(self, pRoot, k):
        if pRoot is None:
            return None

        pre_order = []
        stack = []
        node = pRoot
        while node is not None or stack != []:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            pre_order.append(node.val)
            if len(pre_order) == k:
                print(pre_order)
                return node
            node = node.right
        print(pre_order)
        return None


if __name__ == '__main__':
    s = Solution()

    root1 = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8)))
    # root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(8, TreeNode(4), TreeNode(9))
    # root2 = TreeNode()
    print(s.KthNode(root1, 3))