from collections import Counter

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        alphabet_freq = [0]*26
        freq_freq = [0]*101
        for c in s:
            alphabet_freq[ord(c) - ord('a')] += 1
        for freq in alphabet_freq:
            if freq == 0:
                continue
            freq_freq[freq] += 1
        max_freq_freq = max(freq_freq)
        for i in range(len(freq_freq)):
            if freq_freq[i] == max_freq_freq:
                max_alphabet_freq = i
        result = ""
        for i in range(len(alphabet_freq)):
            if alphabet_freq[i] == max_alphabet_freq:
                result += chr(i + ord('a'))
        return result
