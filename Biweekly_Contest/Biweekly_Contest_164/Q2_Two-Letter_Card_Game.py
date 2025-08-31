from collections import defaultdict
from typing import List

class Solution:
    def score(self, cards: List[str], x: str) -> int:
        compatible_index = defaultdict(int)
        for index, i in enumerate(cards):
            if x == i[0] and x == i[1]:
                compatible_index[index] = 3
                continue
            if x == i[0]:
                compatible_index[index] = 1
            if x == i[1]:
                compatible_index[index] = 2
        compatible_index_one = defaultdict(int)
        index_one_total = 0
        index_one_max_frequent = 0
        compatible_index_two = defaultdict(int)
        index_two_total = 0
        index_two_max_frequent = 0
        both_index = 0
        for key, value in compatible_index.items():
            if value == 1:
                compatible_index_one[cards[key][1]] += 1
                index_one_total += 1
                index_one_max_frequent = compatible_index_one[cards[key][1]] if compatible_index_one[cards[key][1]] > index_one_max_frequent else index_one_max_frequent
            if value == 2:
                compatible_index_two[cards[key][0]] += 1
                index_two_total += 1
                index_two_max_frequent = compatible_index_two[cards[key][0]] if compatible_index_two[cards[key][0]] > index_two_max_frequent else index_two_max_frequent
            if value == 3:
                both_index += 1
        result = 0
        for i in range(both_index+1):
            index_one_result = min((index_one_total+i) // 2, index_one_total + i - max(index_one_max_frequent, i))
            index_two_result = min((index_two_total+(both_index-i)) // 2, index_two_total + (both_index-i) - max(index_two_max_frequent, both_index - i))
            temp_result = index_one_result + index_two_result
            result = temp_result if temp_result > result else result
        return result
