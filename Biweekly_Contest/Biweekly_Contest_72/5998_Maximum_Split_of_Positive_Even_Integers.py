class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        answer = []
        if finalSum%2 != 0:
            return answer
        start = 1
        while(True):
            even = start*2
            if (finalSum >= even):
                if len(answer) > 0 and answer[len(answer)-1] == even:
                    answer[len(answer)-1] += finalSum
                    break
                answer.append(even)
                finalSum -= even
                start += 1
            else:
                answer[len(answer)-1] += finalSum
                break
        return answer