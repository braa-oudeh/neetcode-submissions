# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        if len(lists) == 1: 
            return lists[0]

        middle = len(lists) // 2 
        left = self.mergeKLists(lists[:middle])
        right = self.mergeKLists(lists[middle:])

        return self.mergeTwoLists(left,right)

    def mergeTwoLists(self, arr1, arr2): 
        dummyNode = node = ListNode(0)

        while arr1 and arr2: 
            if arr1.val < arr2.val: 
                node.next = arr1 
                arr1 = arr1.next
            else: 
                node.next = arr2
                arr2 = arr2.next
            node = node.next 
        node.next = arr1 or arr2 
        return dummyNode.next