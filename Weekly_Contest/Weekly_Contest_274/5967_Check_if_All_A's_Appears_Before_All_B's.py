class Solution:
    def checkString(self, s: str) -> bool:
        answer = True
        b_flag = False
        for character in s:
            if b_flag == True and character == "a":
                answer = False
                break
            elif character == "b":
                b_flag = True

        return answer
