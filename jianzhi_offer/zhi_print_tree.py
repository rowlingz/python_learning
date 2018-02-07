# 按之字型打印二叉树
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, elem=None, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        stack1, stack2 = [], []
        stack1.append(pRoot)
        result = []
        while stack1 or stack2:
            s1 = []
            while stack1:
                node = stack1.pop()
                s1.append(node.elem)
                if node.left is not None:
                    stack2.append(node.left)
                if node.right is not None:
                    stack2.append(node.right)

            if s1 != []:
                result.append(s1)

            s2 = []
            while stack2:
                node = stack2.pop()
                s2.append(node.elem)
                if node.right is not None:
                    stack1.append(node.right)
                if node.left is not None:
                    stack1.append(node.left)

            if s2 != []:
                result.append(s2)

        return result


if __name__ == '__main__':
    s = Solution()

    root1 = TreeNode(8, TreeNode(6, TreeNode(9), TreeNode(2, TreeNode(4), TreeNode(7))), TreeNode(7, TreeNode(1), TreeNode(0)))
    # root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(8, TreeNode(9), TreeNode(4))
    root3 = None

    print(s.Print(root2))