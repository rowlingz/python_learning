# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, val= None, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot1 is None or pRoot2 is None:
            return False
        result = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.tree1havetree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def tree1havetree2(self, pRoot1, pRoot2):
        if pRoot2 is None:
            return True
        if pRoot1 is None:
            return False
        if pRoot1.val != pRoot2.val:
            return False

        result = self.tree1havetree2(pRoot1.left, pRoot2.left) and \
                 self.tree1havetree2(pRoot1.right, pRoot2.right)
        return result

    def search(self, pRoot1, pRoot2):
        key = pRoot2.val
        if pRoot1 is None:
            return False
        else:
            if pRoot1.val == key:
                return pRoot1
            else:
                return self.search(pRoot1.left, pRoot2) or self.search(pRoot1.right, pRoot2)


if __name__ == '__main__':
    s = Solution()

    root1 = TreeNode(8, TreeNode(8, TreeNode(9), TreeNode(2, TreeNode(4), TreeNode(7))), TreeNode(7))
    # root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(8, TreeNode(9), TreeNode(4))
    # root2 = TreeNode()
    if s.HasSubtree(root1, root2):
        print('存在')
    else:
        print('bu')

    print(root2.val)