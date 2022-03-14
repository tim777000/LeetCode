class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        num_dict = {}
        for index, num in enumerate(nums):
            if (num not in num_dict.keys()):
                num_dict[num] = [index]
            else:
                num_dict[num].append(index)
        if len(nums) == len(num_dict):
            return 0
        answer = 0
        for num in num_dict:
            if len(num_dict[num]) > 1:
                for i in range(len(num_dict[num])):
                    for j in range(i+1, len(num_dict[num])):
                        if (num_dict[num][i]*num_dict[num][j])%k == 0:
                            answer += 1
        return answer

