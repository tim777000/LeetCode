class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        second_pointer = 0
        for i in t:
            if (second_pointer == len(s)):
                break
            if (i == s[second_pointer]):
                second_pointer += 1
        return second_pointer == len(s)
