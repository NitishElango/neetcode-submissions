# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        start = dummy
        while l1 or l2:
            if l1 and l2:
                sum1 = l1.val + l2.val + carry
            elif l1:
                sum1 = l1.val + carry
            else:
                sum1 = l2.val + carry
            if sum1 > 9:
                sum1-=10
                carry = 1
            else:
                carry = 0
            dummy.next = ListNode(sum1)
            dummy = dummy.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            dummy.next = ListNode(carry)
            dummy = dummy.next
        return start.next
            