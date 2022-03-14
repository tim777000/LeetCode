class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_list = [-1]*26
        for index, c in enumerate(s):
            if char_list[ord(c)-ord('a')] == -1:
                char_list[ord(c)-ord('a')] = index
            else:
                char_list[ord(c)-ord('a')] = -2
        answer_list = [ c for c in char_list if c >= 0 ]
        return min(answer_list) if answer_list else -1

