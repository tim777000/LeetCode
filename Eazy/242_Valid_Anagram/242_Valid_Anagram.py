class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        length_of_s = len(s)
        if (length_of_s != len(t)):
            return False
        character_list = [0]*26
        for i in range(length_of_s):
            character_list[ord(s[i])-ord('a')] += 1
            character_list[ord(t[i])-ord('a')] -= 1

        return set(character_list) == {0}


