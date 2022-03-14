class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length_of_nums = len(nums)
        counter = 0
        while(gcd(length_of_nums, k) != 1):
            counter += 1
            k -= 1
        for i in range(counter):
            self.rotate_target_times(nums, 1)
        self.rotate_target_times(nums, k)
        return

    def rotate_target_times(self, nums: List[int], k: int) -> None:
        length_of_nums = len(nums)
        counter = 0
        temp = nums[length_of_nums-1]
        i = length_of_nums-1
        while(True):
            i = (i+k)%length_of_nums
            temp, nums[i] = nums[i], temp
            counter += 1
            if (counter == length_of_nums):
                break
        return
