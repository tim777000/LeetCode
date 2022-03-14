class Solution:
    def minSteps(self, s: str, t: str) -> int:
        alpha_count = [0]*26
        for character in s:
            alpha_count[ord(character)-ord('a')] += 1
        for character in t:
            alpha_count[ord(character)-ord('a')] -= 1
        return sum( [ abs(count) for count in alpha_count ] )