class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        answer = []
        temp = ""
        for index, character in enumerate(s):
            temp += character
            if ((index + 1)%k == 0):
                answer.append(temp)
                temp = ""
        if (temp != ""):
            temp += fill*(k-len(temp))
            answer.append(temp)

        return answer
