class Solution:
    def replaceDigits(self, s: str) -> str:
        answer = ""
        prev = ''
        sLength = len(s)
        for i in range(0, sLength):
            # index is even
            if i & 1 == 0:
                answer += s[i]
                prev = s[i]
            # index is odd
            else:
                answer += chr(ord(prev) + int(s[i]))
        return answer