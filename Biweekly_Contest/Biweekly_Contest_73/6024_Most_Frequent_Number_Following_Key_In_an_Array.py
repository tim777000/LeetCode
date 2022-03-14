class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        target_dict = {}
        length_of_nums = len(nums)
        for index, num in enumerate(nums):
            if (index == length_of_nums-1):
                break
            if (num != key):
                continue
            if (nums[index+1] not in target_dict.keys()):
                target_dict[nums[index+1]] = 1
            else:
                target_dict[nums[index+1]] += 1
        return max(target_dict, key=target_dict.get)
