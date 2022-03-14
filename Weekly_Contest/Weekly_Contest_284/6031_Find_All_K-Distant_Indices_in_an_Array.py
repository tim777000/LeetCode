class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_list = [index for index, num in enumerate(nums) if num == key]
        length_of_key_list = len(key_list)
        key_list_index = 0
        answer = []
        for index, num in enumerate(nums):
            if (abs(index-key_list[key_list_index]) <= k):
                answer.append(index)
            elif((index > key_list[key_list_index]) and (key_list_index+1) < length_of_key_list):
                key_list_index += 1
                if (abs(index-key_list[key_list_index]) <= k):
                    answer.append(index)
        return answer


