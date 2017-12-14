class Node(object):
    # 创建节点类
    def __init__(self, elem=None, left=None, right=None):
        self.elem = elem
        self.left = left
        self.right = right


class Tree(object):
    # 创建树类
    def __init__(self, root=None):
        self.root = root

    def pre_order(self, root):
        if not root:
            return
        print(root.elem)
        self.pre_order(root.left)
        self.pre_order(root.right)

    def mid_order(self, root):
        if not root:
            return
        self.mid_order(root.left)
        print(root.elem)
        self.mid_order(root.right)

    def after_order(self, root):
        if not root:
            return
        self.after_order(root.left)
        self.after_order(root.right)
        print(root.elem)

    def layer_order(self, root):
        if not root:
            return
        myqueue = []
        myqueue.append(root)
        s = []
        while myqueue:
            node = myqueue.pop(0)
            s.append(node.elem)
            if node.left is not None:
                myqueue.append(node.left)
            if node.right is not None:
                myqueue.append(node.right)


        return s

    def micro_layer(self, root):
        list = []
        layer_node = [root]
        while layer_node :
            temp_list = []
            temp_layer = []
            for n in layer_node :
                if n.left :
                    temp_list.append(n.left)
                if n.right :
                    temp_list.append(n.right)
                temp_layer.append(n.elem)
            list.append(temp_layer)
            layer_node = temp_list
        return list




s = Node(1, Node(2, Node(4), Node(6)), Node(3,Node(5),Node(7)))
t = Tree()
print(t.micro_layer(s))