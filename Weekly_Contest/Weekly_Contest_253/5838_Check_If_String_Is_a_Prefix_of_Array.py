class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        sLength = len(s)
        answer = False
        tempString = ""
        for word in words:
            tempString += word
            if (len(tempString) > sLength):
                break
            if (len(tempString) == sLength):
                if (tempString == s):
                    answer = True
                    break
        return answer