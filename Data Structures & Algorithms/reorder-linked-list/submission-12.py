# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: 
            return 
        
        if head.next is None: 
            return

        slow = head 
        fast = head 
        while fast and fast.next and fast.next.next: 
            slow = slow.next 
            fast = fast.next.next 
        # NOW SLOW IS THE MIDDLE INDEX, we can now slice it into two lists
        secondLinkedList = slow.next 
        slow.next = None 
        reversedLinkedList = self.reverseList(secondLinkedList)        
        curr = head
        currReversed = reversedLinkedList
        while curr and currReversed: 
            tmp = curr.next 
            tmp2 = currReversed.next
            curr.next = currReversed
            currReversed.next = tmp
            curr = tmp
            currReversed = tmp2

        # Now get the remainder of currReversed
        curr = head 
        while curr.next :
            curr = curr.next 
        curr.next = currReversed
            

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head 
        while curr: 
            tmp1 = curr.next 
            curr.next = prev 
            prev = curr 
            curr = tmp1 
        return prev
