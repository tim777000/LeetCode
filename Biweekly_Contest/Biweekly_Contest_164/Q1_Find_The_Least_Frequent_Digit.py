from collections import defaultdict

class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        digit_frequent = defaultdict(int)
        while n > 0:
            digit_frequent[n % 10] += 1
            n //= 10
        min_frequent = 11
        for key, value in digit_frequent.items():
            if value == 0:
                continue
            if (value == min_frequent and key < result) or value < min_frequent:
                result = key
                min_frequent = value
        return result
