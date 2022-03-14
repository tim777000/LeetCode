class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        answer = ""
        for word in words:
            if (self.check_palindrome(word)):
                answer = word
                break
        return answer
    def check_palindrome(self, word: str) -> bool:
        answer = True
        length_of_word = len(word)
        for i in range(0, length_of_word//2):
            if (word[i] != word[length_of_word-1-i]):
                answer = False
                break
        return answer

