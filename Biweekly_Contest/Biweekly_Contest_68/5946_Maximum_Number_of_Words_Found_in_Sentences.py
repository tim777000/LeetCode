class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_number_of_word = 0
        for sentence in sentences:
            word_count = sentence.count(' ') + 1
            if (word_count > max_number_of_word):
                max_number_of_word = word_count
        return max_number_of_word