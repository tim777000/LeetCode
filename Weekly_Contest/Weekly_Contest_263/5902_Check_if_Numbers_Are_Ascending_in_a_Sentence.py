class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        wordList = s.split()

        numberList = [int(word) for word in wordList if word.isdigit() == True]

        answer = all(i < j for i, j in zip(numberList, numberList[1:]))

        return answer

