from typing import List
from math import inf

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        result = inf
        for task in tasks:
            if (task[0] + task[1] < result):
                result = task[0] + task[1]
        return result
