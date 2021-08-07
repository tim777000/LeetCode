class Solution:
    def makeFancyString(self, s: str) -> str:

        counter = 1
        stringList = list(s)
        answerList = []
        leadingChar = stringList[0]

        for i in range(0, len(stringList)):
            if (i == 0):
                answerList.append(stringList[i])
                continue
            if (stringList[i] == leadingChar):
                counter += 1
            else:
                leadingChar = stringList[i]
                counter = 1
            if (counter != 3):
                answerList.append(stringList[i])
            else:
                counter -= 1

        answerString = ''.join(answerList)

        return answerString