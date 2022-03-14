class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = ""
        space = 0
        length_of_spaces = len(spaces)
        for index, character in enumerate(s):
            if (space < length_of_spaces and index == spaces[space]):
                answer += (" " + character)
                space += 1
            else:
                answer += character
        return answer

