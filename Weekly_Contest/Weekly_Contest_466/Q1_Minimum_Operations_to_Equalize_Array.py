from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        nums_unique = set(nums)
        if (len(nums_unique) == 1):
            return 0
        return 1
