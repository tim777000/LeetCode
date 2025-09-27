from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        alphabet_s = defaultdict(lambda: None)
        alphabet_t = defaultdict(lambda: None)
        s_length = len(s)
        for i in range(s_length):
            if alphabet_s[s[i]] is None and alphabet_t[t[i]] is None:
                alphabet_s[s[i]] = t[i]
                alphabet_t[t[i]] = s[i]
            elif alphabet_s[s[i]] != t[i] or alphabet_t[t[i]] != s[i]:
                return False
        return True
