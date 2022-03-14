class Solution:
    def minimumSum(self, num: int) -> int:
        digit_list = []
        answer = 0
        for i in range(1, 5):
            digit_list.append((num%(10**i))//(10**(i-1)))
        for index, number in enumerate(sorted(digit_list)):
            if (index < 2):
                answer += number*10
            else:
                answer += number
        return answer


