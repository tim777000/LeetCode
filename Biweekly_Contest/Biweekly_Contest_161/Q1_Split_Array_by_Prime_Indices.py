class Solution:
    def splitArray(self, nums: List[int]) -> int:
        A = 0
        B = 0
        for index, i in enumerate(nums):
            if (self.isPrime(index)):
                A += i
            else:
                B += i
        return abs(A - B)
    def isPrime(self, i: int) -> bool:
        if i < 2:
            return False
        square_root = sqrt(i)
        start = 2
        while start <= square_root:
            if i % start == 0:
                return False
            start += 1
        return True