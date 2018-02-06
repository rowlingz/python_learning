
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinarysortTree:
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        bt = self._root
        while bt:
            if key < bt.data:
                bt = bt.left
            elif key > bt.data:
                bt = bt.right
            else:
                return True
        return False

    def insert(self, key):
        bt = self._root
        if bt is None:
            self._root = Node(key)
            return
        while True:
            entry = bt.data
            if key < entry:
                if bt.left is None:
                    bt.left = Node(key)
                    return
                bt = bt.left
            elif key > entry:
                if bt.right is None:
                    bt.right = Node(key)
                    return
                bt = bt.right
            else:
                bt.data = key
                return

    def delet(self, key):
        # 定义删除结点为q,其父结点为p
        p, q = None, self._root
        if q is None:
            print("空树！")
            return

        # 找到要删除的结点，p为q的父结点，（包含q为根节点，则p为None）
        while q is not None and q.data != key:
            p = q
            if key < q.data:
                q = q.left
            else:
                q = q.right
            if q is None:
                print("当前树没有" + str(key))
                return

        # 删除结点
        # q没有左结点
        if q.left is None:
            if p is None:
                self._root = q.right
            elif q is p.left:
                p.left = q.right
            else:
                p.right = q.right
            return

        # q有左子树，找到左子树的最右结点，记为r，用q的右子树作为r的右子树，
        r = q.left
        while r.right is not None:
            r = r.right
        r.right = q.right

        # 判断q处的位置，用q.left 去取代q的位置
        if p is None:
            self._root = q.left
        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left

    def pre_order(self):
        output = []
        stack = []
        node = self._root
        while node is not None or stack != []:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            output.append(node.data)
            node = node.right

        return output


if __name__ == '__main__':

    lis = [62, 58, 88, 48, 73, 99, 35, 51, 93, 29, 37, 49, 56, 36, 50]
    binary_tree = BinarysortTree()
    for i in range(len(lis)):
        binary_tree.insert(lis[i])

    print(binary_tree.pre_order())

    binary_tree.insert(100)
    print(binary_tree.pre_order())

    binary_tree.delet(50)
    print(binary_tree.pre_order())

    binary_tree.delet(1)


