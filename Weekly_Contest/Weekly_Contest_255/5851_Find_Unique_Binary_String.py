class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        binaryLength = len(nums)
        answer = ""
        for i in range(0, binaryLength):
            if (nums[i][i] == "0"):
                answer += "1"
            else:
                answer += "0"

        return answer