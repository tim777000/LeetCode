class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        number_of_zeros = nums.count(0)
        number_of_ones = nums.count(1)
        length_of_nums = len(nums)
        max_records = []
        max_records.append(0 + number_of_ones)
        for index, num in enumerate(nums):
            if (num == 0):
                max_records.append(max_records[index]+1)
            else:
                max_records.append(max_records[index]-1)
        max_value = max(max_records)
        answer = [ index for index, value in enumerate(max_records) if value == max_value ]

        return answer

