from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split(' ')
        pattern_length = len(pattern)
        s_length = len(s_words)
        if pattern_length != s_length:
            return False
        correspond_pattern = defaultdict(lambda: None)
        correspond_s = defaultdict(lambda: None)
        pattern_length = len(pattern)
        for i in range(pattern_length):
            if correspond_pattern[pattern[i]] is None and correspond_s[s_words[i]] is None:
                correspond_pattern[pattern[i]] = s_words[i]
                correspond_s[s_words[i]] = pattern[i]
            elif correspond_pattern[pattern[i]] != s_words[i] or correspond_s[s_words[i]] != pattern[i]:
                return False
        return True
