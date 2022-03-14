class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        index = -1
        numsLength = len(nums)

        for i in range(0, numsLength):
            if (i % 10 == nums[i]):
                index = i
                break

        return index