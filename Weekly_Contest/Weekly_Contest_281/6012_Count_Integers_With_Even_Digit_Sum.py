class Solution:
    def countEven(self, num: int) -> int:
        answer = 0
        for i in range(1, num+1):
            temp_value = 0
            while (i >= 10):
                temp_value += i%10
                i = i//10
            if (temp_value+i)%2 == 0:
                answer += 1

        return answer