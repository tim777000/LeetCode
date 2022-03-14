import re

class Solution:
    def countValidWords(self, sentence: str) -> int:
        sentenceList = filter(None, sentence.split(' '))
        regularExpression = "\A[a-z]*([a-z]-[a-z])?[a-z]*[!,.]?\Z"


        comparisonList = [re.match(regularExpression, word) for word in sentenceList]
        
        return sum(comparison is not None for comparison in comparisonList)