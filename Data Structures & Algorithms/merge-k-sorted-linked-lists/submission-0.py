# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) < 2:
            return
        for i in range(len(lists)-1):
            h1, h2  = lists[i], lists[i+1]
            temp = ListNode()
            start = temp
            while h1 and h2:
                if h1.val <= h2.val:
                    temp.next = h1
                    temp = temp.next
                    h1 = h1.next
                else:
                    temp.next = h2
                    temp = temp.next
                    h2 = h2.next
            if h1:
                temp.next = h1
            elif h2:
                temp.next = h2
            lists[i+1] = start.next
        return start.next
