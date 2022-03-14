# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp = head
        linked_list_counter = 0
        while temp != None:
            temp = temp.next
            linked_list_counter += 1
        if (linked_list_counter == 1):
            return True
        half_head_count = ceil(linked_list_counter/2)+1
        temp = head
        for i in range(half_head_count):
            half_head = temp
            temp = temp.next
        half_head = self.revesed_linked_list(half_head)
        for i in range(linked_list_counter//2):
            if (head.val != half_head.val):
                return False
            head = head.next
            half_head = half_head.next
        return True

    def revesed_linked_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = None
        while head != None:
            temp_pre_head = pre_head
            pre_head = head
            head = head.next
            pre_head.next = temp_pre_head
        return pre_head

