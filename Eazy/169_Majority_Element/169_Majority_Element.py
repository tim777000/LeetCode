from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        for index, i in enumerate(nums):
            if index == 0:
                result = i
                count = 1
                continue
            if i == result:
                count += 1
            else:
                count -= 1
            if count == 0:
                result = i
                count = 1
        return result
