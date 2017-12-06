# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
    # 返回构造的TreeNode根节点
def get_left(pre, tin):
    if pre is None:
        return None, None
    n = len(pre)
    for i in range(n):
        if pre[0] == tin[i]:
            if i == 0:
                new_pre1, new_tin1 = None, None
            elif i <= n - 1:
                new_pre1, new_tin1 = pre[1:i + 1], tin[:i]
            break
    return new_pre1, new_tin1


def get_right(pre, tin):
    if pre is None:
        return None, None
    n = len(pre)
    for i in range(n):
        if pre[0] == tin[i]:
            if i == n - 1:
                new_pre2, new_tin2 = None, None
            elif i < n - 1:
                new_pre2, new_tin2 = pre[i + 1:], tin[i + 1:]
            break
    return new_pre2, new_tin2

def reConstructBinaryTree(pre, tin):
    # write code here
    if pre is None:
        return None
    n = len(pre)
    root = TreeNode(pre[0])
    if n == 1:
        return root
    else:
        pre_left, tin_left = get_left(pre, tin)
        root.left = reConstructBinaryTree(pre_left, tin_left)
        pre_right, tin_right = get_right(pre, tin)
        root.right = reConstructBinaryTree(pre_right, tin_right)
    return root



pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]

s = reConstructBinaryTree(pre, tin)
print(s)
