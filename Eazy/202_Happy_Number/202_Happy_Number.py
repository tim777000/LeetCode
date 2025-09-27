class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        change_n = self.split_and_square_and_add(n)
        while(change_n != 1):
            if (change_n in seen):
                return False
            seen.add(change_n)
            change_n = self.split_and_square_and_add(change_n)
        return True
    def split_and_square_and_add(self, n: int) -> int:
        add = 0
        while(n != 0):
            add = add + (n % 10)**2
            n = n // 10
        return add
