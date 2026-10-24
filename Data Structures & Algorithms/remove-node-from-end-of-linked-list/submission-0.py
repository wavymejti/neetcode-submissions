# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        res = []
        while cur:
            res.append(cur)
            cur = cur.next
        removeIndex = len(res) - n
        if removeIndex == 0:
            return head.next
        res[removeIndex - 1].next = res[removeIndex].next
        return head