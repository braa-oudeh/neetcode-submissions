# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_1_string = ""
        l_2_string = ""

        curr_1 = l1
        while curr_1: 
            l_1_string += str(curr_1.val)
            curr_1 = curr_1.next
        reversed_l1 = l_1_string[::-1]
        curr_2 = l2
        while curr_2: 
            l_2_string += str(curr_2.val)
            curr_2 = curr_2.next
        reversed_l2 = l_2_string[::-1]

        res = int(reversed_l1) + int(reversed_l2)
        reversed_res = str(res)[::-1]
        dummyNode = ListNode(0)
        head_node = dummyNode
        for i in range(len(reversed_res)):
            node = ListNode(int(reversed_res[i]))
            head_node.next = node
            head_node = head_node.next
        return dummyNode.next
