# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while (node.next != None):
            node.val = node.next.val
            prevous_node = node
            node = node.next
        prevous_node.next = None
        return