class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        answer = 0
        temp = 0
        for i in arr2:
            temp ^= i
        for i in arr1:
            i &= temp
            answer ^= i
        return answer