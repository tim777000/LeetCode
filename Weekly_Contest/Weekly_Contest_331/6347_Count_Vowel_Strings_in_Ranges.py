class Solution:
    vowels = ['a', 'e', 'i', 'o', 'u']

    # O(n)
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_arr = self.prefix_sum(words)
        answer = []
        for start, end in queries:
            answer.append(prefix_arr[end] - prefix_arr[start] + self.vowel_check(words[start]))
        return answer

    # O(n)
    def prefix_sum(self, words: List[str]) -> List[int]:
        prefix_arr = []
        for index, word in enumerate(words):
            if index == 0:
                prefix_arr.append(self.vowel_check(word))
                continue
            prefix_arr.append(prefix_arr[index-1] + self.vowel_check(word))
        return prefix_arr
    
    # O(1)
    def vowel_check(self, word: str) -> int:
        if (word[0] in self.vowels and word[-1] in self.vowels):
            return 1
        return 0