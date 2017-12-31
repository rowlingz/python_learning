# 树
class Node():
    def __init__(self, x = None, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right


class Tree():
    def __init__(self, root = None):
        self.root = root

    def depth_search(self, root):
        if not root:
            return
        print(root.val)
        self.depth_search(root.left)
        self.depth_search(root.right)

    def depth_search_nonrec(self, root):
        out_list = []
        stack = []
        stack.append(root)
        while len(stack) >= 1:
            while root:
                out_list.append(root.val)
                stack.append(root.right)
                root = root.left
            root = stack.pop()
        return out_list


s = Node(1, Node(2, Node(4), Node(6)), Node(3,Node(5),Node(7)))
t = Tree()

t.depth_search(s)
print(t.depth_search_nonrec(s))


class ListNode():
    def __init__(self, val = None):
        self.val = val
        self.next = None


def reverse_list(head):
    while head is None or head.next is None:
        return head
    newhead = ListNode()
    while head is not None:
        p = head
        head = head.next
        p.next = newhead
        newhead = p

    return newhead


p1 = ListNode(1)
p1.next = ListNode(3)
p1.next.next = ListNode(5)

reverse_list(p1)