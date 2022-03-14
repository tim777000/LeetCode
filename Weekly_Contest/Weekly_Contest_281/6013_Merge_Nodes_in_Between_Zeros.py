# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = None
        temp_head = answer
        temp_value = 0
        isStart = True
        isAnswer = False
        while (head != None):
            if (head.val != 0):
                isStart = False
                temp_value += head.val
            else:
                if (not isStart):
                    if (not isAnswer):
                        answer = ListNode(temp_value)
                        isAnswer = True
                        temp_head = answer
                    else:
                        temp_head.next = ListNode(temp_value)
                        temp_head = temp_head.next
                temp_value = 0
            head = head.next
        return answer