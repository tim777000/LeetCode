class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        records_table = [False]*11
        answer = original
        for num in nums:
            remainder = num%original
            quotient = num//original
            if (quotient == 0):
                continue
            if (remainder == 0 and (quotient&(quotient-1) == 0)):
                records_table[floor(log(quotient, 2))] = True

        for index, record in enumerate(records_table):
            if record == False:
                answer *= (2**index)
                break

        return answer
