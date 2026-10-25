# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = list1
        curr_2 = list2 
        dummy = node = ListNode()
        while curr_1 and curr_2: 
            if curr_1.val < curr_2.val: 
                node.next = curr_1
                curr_1 = curr_1.next 
            else:
                node.next = curr_2
                curr_2 = curr_2.next
            node = node.next
        
        node.next = curr_1 or curr_2 
        return dummy.next