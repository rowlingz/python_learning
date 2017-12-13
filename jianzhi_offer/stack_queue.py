# -*- coding:utf-8 -*-
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。


class Stack(object):
    # 创建一个栈
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        if self.elems == []:
            return None
        popelem = self.elems.pop()
        return popelem


class Solution:
    """应用两个栈实现队列的push pop操作"""
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def push(self, node):
        # 如果栈1中为空，将栈2中的存在元素重排进栈1，保证入队前，已有元素在栈1中按入队顺序排列
        if self.stack1.is_empty():
            while not self.stack2.is_empty():
                self.stack1.push(self.stack2.pop())
        self.stack1.push(node)

    def pop(self):
        # 如果栈2 为空，将栈1中已经入队的元素压入栈2后，由栈2弹出队头
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()



t = Solution()
t.push(1)
t.push(2)
t.push(3)
print(t.pop())
t.push(4)
print(t.pop())
t.push(5)
print(t.pop())
print(t.pop())
print(t.pop())
