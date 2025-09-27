from typing import List

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        non_dup_nums = set(nums)
        sorted_non_dup_nums = sorted(non_dup_nums, reverse=True)
        result = []
        for i in range(k):
            if (i >= len(sorted_non_dup_nums)):
                break
            result.append(sorted_non_dup_nums[i])
        return result
