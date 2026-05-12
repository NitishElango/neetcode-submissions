# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #find the length of the linked  list
        #once we hit length - n +1, we remove the element from the list
        #return head of linked list
        dummy = ListNode(next = head)
        curr = head
        prev = dummy
        length = 0
        length2 = 1

        while curr:
            curr = curr.next
            length+=1
        curr = head
        while curr:
            if(length - n + 1 == length2):
                prev.next = curr.next
                curr = curr.next
                length2+=1
            else:
                prev = curr
                curr = curr.next
                length2+=1
        return dummy.next

