class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabetSet = {i for i in sentence}
        return len(alphabetSet) == 26