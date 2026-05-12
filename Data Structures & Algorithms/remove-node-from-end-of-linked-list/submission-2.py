# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length +=1
        
        target = length - n - 1

        ptr = ListNode()
        ptr.next = head
        start = ptr
        count = -1
        while ptr and ptr.next:
            if count == target:
                ptr.next = ptr.next.next
            ptr = ptr.next
            count +=1
        
        return start.next
