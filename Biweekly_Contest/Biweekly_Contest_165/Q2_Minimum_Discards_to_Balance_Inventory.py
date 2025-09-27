from typing import List
from collections import defaultdict

class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        storage = defaultdict(int)
        left, right = 0, 0
        result = 0
        while right < len(arrivals):
            if (right - left + 1) >  w:
                storage[arrivals[left]] -= 1
                left += 1
            if storage[arrivals[right]] == m:
                result += 1
                arrivals[right] = -1
            else:
                storage[arrivals[right]] += 1
            right += 1
        return result
