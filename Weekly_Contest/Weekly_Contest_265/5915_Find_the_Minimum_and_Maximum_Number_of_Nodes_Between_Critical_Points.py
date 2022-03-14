# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        criticalPointsList = []
        preValue = -1
        nodesCounter = 1

        while(head != None):
            if(nodesCounter != 1 and self.checkCriticalPoint(preValue, head)):
                criticalPointsList.append(nodesCounter)
            preValue = head.val
            head = head.next
            nodesCounter += 1

        criticalPointsListLength = len(criticalPointsList)
        if (criticalPointsListLength >= 2):
            distanceList = [criticalPointsList[i+1] - criticalPointsList[i] for i in range(0, criticalPointsListLength) if i+1 < criticalPointsListLength]
            return [min(distanceList), criticalPointsList[criticalPointsListLength-1] - criticalPointsList[0]]

        return[-1, -1]

    def checkCriticalPoint(self, preValue: int, head: Optional[ListNode]) -> bool:
        if (head.next == None):
            return False
        elif (preValue > head.val and head.val < head.next.val):
            return True
        elif (preValue < head.val and head.val > head.next.val):
            return True
        else:
            return False