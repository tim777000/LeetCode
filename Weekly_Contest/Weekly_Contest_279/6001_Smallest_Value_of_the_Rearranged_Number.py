class Solution:
    def smallestNumber(self, num: int) -> int:
        if (num > 0):
            num_string = sorted(str(num))
        else:
            num_string = sorted(str(-num), reverse=True)

        if (num_string[0] == "0"):
            for index, digit in enumerate(num_string):
                if (digit != "0" and index != 0):
                    num_string[0], num_string[index] = num_string[index], num_string[0]
                    break

        answer = int("".join(num_string))

        return answer if num > 0 else -answer



