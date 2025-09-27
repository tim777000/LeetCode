from types import List

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        average = sum(nums) / len(nums)
        nums_set = set(nums)
        candidate = int(average) + 1 if int(average) + 1 > 0 else 1
        while (candidate in nums_set):
            candidate += 1
        return candidate
