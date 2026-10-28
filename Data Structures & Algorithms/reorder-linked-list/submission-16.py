# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head 
        while fast and fast.next: 
            slow = slow.next 
            fast = fast.next.next 

        otherHalf = slow.next 
        slow.next = None 
        
        # Sort the Other Half 
        prev = None 
        curr = otherHalf 

        while curr: 
            tmp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = tmp 
        
        sortedHalf = prev 

        l1 = head 
        l2 = sortedHalf

        while l1 and l2:
            tmp1 = l1.next
            tmp2 = l2.next 
            l1.next = l2 
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2 

        