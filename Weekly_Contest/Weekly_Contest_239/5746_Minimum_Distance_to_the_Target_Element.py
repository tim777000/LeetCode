class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        numsLength = len(nums)
        dist = -1
        for i in range(0, numsLength):
            if target == nums[i]:
                if dist == -1:
                    dist = abs(i - start)
                else:
                    if abs(i - start) < dist:
                        dist = abs(i - start)
                    else:
                        break
        return dist