class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        answer = 0
        num_1, num_2 = num1, num2
        while(True):
            if (num_1 == 0 or num_2 == 0):
                break
            max_num = num_1 if num_1 >= num_2 else num_2
            min_num = num_1 if num_1 < num_2 else num_2
            max_num -= min_num
            num_1, num_2 = max_num, min_num
            answer += 1

        return answer
