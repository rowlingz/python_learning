# -*- coding:utf-8 -*-
# 输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度
class Node(object):
    # 创建节点类
    def __init__(self, elem=None, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        n_r, n_l = 1, 1
        if pRoot.left:
            n_l += self.TreeDepth(pRoot.left)
        if pRoot.right:
            n_r += self.TreeDepth(pRoot.right)

        return max(n_r, n_l)


s = Node(1, Node(2, Node(4), Node(6,Node(8))), Node(3,Node(5),Node(7)))
t = Solution()
print(t.TreeDepth(s))