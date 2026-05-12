# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # iterate to  half point of the list
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        prev = None

        while s:
            temp = s.next
            s.next = prev
            prev = s
            s = temp
        
        start = head
        dummy = ListNode(next = head)
        count = 0

        while start and prev:
            if count % 2 == 0:
                print(start.val)
                dummy.next = start
                dummy = dummy.next
                start = start.next
                count +=1
            else:
                print(prev.val)
                dummy.next = prev
                dummy = dummy.next
                prev = prev.next
                count +=1

