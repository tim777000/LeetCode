# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        pointer_one = head.next
        pointer_two = head.next.next
        has_loop = False
        while(pointer_one != None and pointer_two != None):
            if pointer_one == pointer_two:
                has_loop = True
                break
            if pointer_two.next == None:
                break
            pointer_one = pointer_one.next
            pointer_two = pointer_two.next.next
        if not has_loop:
            return None
        pointer_two = pointer_two.next
        loop_counter = 1
        while(pointer_one != pointer_two):
            pointer_two = pointer_two.next
            loop_counter += 1
        pointer_one = head
        for i in range(loop_counter):
            pointer_one = pointer_one.next
        pointer_two = head
        while(pointer_one != pointer_two):
            pointer_one = pointer_one.next
            pointer_two = pointer_two.next
        return pointer_one