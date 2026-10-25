# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Transform our list of lists into a big list 
        new_list = []
        for i in range(len(lists)): 
            curr = lists[i]
            while curr: 
                new_list.append(curr.val)
                curr = curr.next 
        sorted_list = sorted(new_list)
        if sorted_list:
            dummyNode = ListNode(sorted_list[0])
            currNode = dummyNode

            for i in range(1,len(sorted_list)): 
                node = ListNode(sorted_list[i])
                currNode.next = node 
                currNode = currNode.next
            return dummyNode
        