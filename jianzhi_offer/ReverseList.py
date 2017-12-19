class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1
        p1 = pHead1
        p2 = pHead2
        newHead = ListNode(None)
        newp = newHead
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                newp.next = ListNode(p1.val)
                newp = newp.next
                p1 = p1.next
                continue
            if p2.val < p1.val:
                newp.next = ListNode(p2.val)
                newp = newp.next
                p2 = p2.next
                continue
        if p1 is not None:
            newp.next = p1
        if p2 is not None:
            newp.next = p2
        newHead = newHead.next
        return newHead



p1 = ListNode(1)
p1.next = ListNode(3)
p1.next.next = ListNode(5)

p2 = ListNode(2)
p2.next = ListNode(4)
p2.next.next = ListNode(6)

s = Solution()
print(s.Merge(p1, p2))
