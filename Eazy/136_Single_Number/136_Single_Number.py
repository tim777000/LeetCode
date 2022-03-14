class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        return 2*sum(nums_set) - sum(nums)