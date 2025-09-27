from collections import defaultdict
from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        first_location = defaultdict(lambda:-1)
        for index, i in enumerate(nums):
            if (i in first_location and (index - first_location[i]) <= k):
                return True
            first_location[i] = index
        return False
