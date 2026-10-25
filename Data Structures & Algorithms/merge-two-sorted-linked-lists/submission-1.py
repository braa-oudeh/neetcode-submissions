# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode()
        head = dummyNode
        curr1 = list1 
        curr2 = list2 
        while curr1 and curr2: 
            if curr1.val <= curr2.val: 
                head.next = curr1 
                curr1 = curr1.next 
            else: 
                head.next = curr2
                curr2 = curr2.next 
            head = head.next 
        if curr1 and not curr2: 
            head.next = curr1
        else:
            head.next = curr2 
        return dummyNode.next