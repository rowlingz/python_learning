
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []
        quene = []
        quene.append(root)
        output_array = []
        while quene:
            node = quene.pop(0)
            output_array.append(node.val)
            if node.left:
                quene.append(node.left)
            if node.right:
                quene.append(node.right)
        return output_array