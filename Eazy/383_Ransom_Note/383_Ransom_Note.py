from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_alphabet_count = defaultdict(int)
        for i in magazine:
            magazine_alphabet_count[i] += 1
        for i in ransomNote:
            magazine_alphabet_count[i] -= 1
            if magazine_alphabet_count[i] < 0:
                return False
        return True
