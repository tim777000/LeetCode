# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        pointer_one = head.next
        pointer_two = head.next.next
        while(pointer_one != None and pointer_two != None):
            if pointer_one == pointer_two:
                return True
            if pointer_two.next == None:
                break
            pointer_one = pointer_one.next
            pointer_two = pointer_two.next.next

        return False