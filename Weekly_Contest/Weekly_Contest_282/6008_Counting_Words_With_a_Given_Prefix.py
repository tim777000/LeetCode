class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        length_of_pref = len(pref)
        answer = 0
        for word in words:
            length_of_word = len(word)
            if (length_of_word < length_of_pref):
                continue
            flag = True
            for i in range(length_of_pref):
                if (word[i] != pref[i]):
                    flag = False
                    break
            answer = answer+1 if flag else answer

        return answer

