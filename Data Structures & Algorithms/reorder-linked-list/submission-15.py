# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head 

        while fast and fast.next:
            slow = slow.next  
            fast = fast.next.next 

        nextHead = slow.next 
        slow.next = None 

        curr = nextHead 
        prev = None 
        while curr: 
            tmp1 = curr.next 
            curr.next = prev
            prev = curr
            curr = tmp1

        second = prev 
        first = head 

        while first and second: 
            tmp1,tmp2 = first.next, second.next 
            first.next = second 
            second.next = tmp1 
            first, second = tmp1, tmp2 
         