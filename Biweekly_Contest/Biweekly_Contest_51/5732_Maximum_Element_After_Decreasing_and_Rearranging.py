class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arrLength = len(arr)
        arr.sort()
        for i in range(0, arrLength):
            if i == 0:
                prev = 1
                continue
            else:
                if arr[i] > prev:
                    prev = prev+1
                elif arr[i] < prev:
                    break
        return prev

