## 输入某二叉树的前序遍历和中序遍历的结果，
# 请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
# 则重建二叉树并返回。

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = xgit git
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0 or pre == None :
            return None
        root = TreeNode(pre[0])
        ## 获取左子树的前序遍历
        child_map = self.getChildRoot(pre, tin)
        ## 分别获取左子树和右子树的前序遍历和中序遍历
        pre_left = child_map['pre_left']
        tin_left = child_map['tin_left']
        ## 递归调用,获取左子树
        root.left = self.reConstructBinaryTree(pre_left, tin_left)
        
        pre_right = child_map['pre_right']
        tin_right = child_map['tin_right']
        root.right = self.reConstructBinaryTree(pre_right, tin_right)
        return root
        
        
    ## 找到子树
    def getChildRoot(self, pre, tin) :
        child = {}
        root = pre[0]
        pre_left = []
        tin_left = []
        pre_right = []
        tin_right = []
        ## 中序遍历是否遍历到了根
        flag = False
        for i in tin :
            if i != root and flag != True:
                tin_left.append(i)
            elif i == root :
                flag = True
                continue
            else :
                tin_right.append(i)

        for i in pre :
            if i in tin_left:
                pre_left.append(i)
            elif i != root :
                pre_right.append(i)
        child['pre_left'] = pre_left
        child['pre_right'] = pre_right
        child['tin_left'] = tin_left
        child['tin_right'] = tin_right
        return child


## test
pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
s = Solution()
root = s.reConstructBinaryTree(pre, tin)

print(root)
