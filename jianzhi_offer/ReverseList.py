class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):


        while pHead2.next is not None:
            p1 = pHead1
            p2 = pHead2
            if p2.val <= p1.val:
                new = ListNode(p2.val)
                new.next = p1
                p1.next = new
                pHead2 = pHead2.next
                continue
            if p2.val > p1.val:
                pHead1 = pHead1.next
                continue
        return pHead1


p1 = ListNode(1)
p1.next = ListNode(3)
p1.next.next = ListNode(5)

p2 = ListNode(2)
p2.next = ListNode(4)
p2.next.next = ListNode(6)

s = Solution()
print(s.Merge(p1, p2))
