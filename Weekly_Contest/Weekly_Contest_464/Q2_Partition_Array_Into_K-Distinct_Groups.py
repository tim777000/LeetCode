from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        nums_len = len(nums)
        if (nums_len % k != 0):
            return False
        nums_group = nums_len // k
        nums_dict = [0] * (10**5+1)
        for i in nums:
            nums_dict[i] += 1
        for i in nums_dict:
            if (i > nums_group):
                return False
        return True
