# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None: 
            return None 
        
        reversedList = self.reverseLinkedList(head)
        curr = reversedList
        prev = None
        i = 1 
        if i == n: 
            reversedList = reversedList.next 
            unreversedList = self.reverseLinkedList(reversedList)
            return unreversedList
        while curr:  
            if i == n: 
                prev.next = curr.next 
            i+= 1 
            prev = curr
            curr = curr.next 
        unreversedList = self.reverseLinkedList(reversedList)

        return unreversedList
    def reverseLinkedList(self, head: Optional[ListNode]) -> Optional[listNode]: 
        prev = None 
        curr = head 
        while curr: 
            tmp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = tmp 
        return prev 