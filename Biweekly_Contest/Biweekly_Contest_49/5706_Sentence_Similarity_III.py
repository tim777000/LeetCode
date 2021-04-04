class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        SOne, STwo = sentence1.split(' '), sentence2.split(' ')
        LOne, LTwo = len(SOne), len(STwo)

        if LOne == LTwo:
            return SOne == STwo
        else:
            if LOne < LTwo:
                return self.areSentencesSimilar(sentence2, sentence1)
            else:
                i = 0
                while i < LTwo and STwo[i] == SOne[i]:
                    i+=1
                while i < LTwo and STwo[i] == SOne[LOne-LTwo+i]:
                    i+=1
                return i == LTwo