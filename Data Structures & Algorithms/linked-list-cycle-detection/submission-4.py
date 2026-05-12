# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prev = ListNode()
        prev.next = head
        while prev != head and head:
            if head.next == None:
                return False
            head = head.next.next
            prev = prev.next
        if not head:
            return False
        return True
