# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_node = None
        while(head != None):
            temp_node = pre_node
            pre_node = head
            head = head.next
            pre_node.next = temp_node
        return pre_node