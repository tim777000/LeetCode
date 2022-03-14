class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index, num in enumerate(nums):
            if (target - num) in nums_dict.keys():
                return [index, nums_dict[target-num]]
            nums_dict[num] = index