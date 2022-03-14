class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while_counter = 0
        length_of_nums = len(nums)
        start_flag = False
        for index, num in enumerate(nums):
            if (num == 0 and start_flag == False):
                while_counter = index
                start_flag = True
            if (num == 0):
                while(while_counter < length_of_nums and nums[while_counter] == 0):
                    while_counter += 1
                if (while_counter < length_of_nums):
                    nums[index], nums[while_counter] = nums[while_counter], nums[index]
            if (while_counter == length_of_nums):
                break
        return


