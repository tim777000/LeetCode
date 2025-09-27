class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if (num & 1) == 0:  # Check if the number is even
                result |= num
        return result
