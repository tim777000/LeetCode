class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        answer = []
        counterStart = 0
        numsLength = len(nums)
        counterEnd = numsLength - 1

        while(counterStart < counterEnd):
            answer.append(nums[counterStart])
            counterStart += 1
            answer.append(nums[counterEnd])
            counterEnd -= 1

        if (counterStart == counterEnd):
            answer.append(nums[counterStart])

        return answer