from collections import defaultdict
from typing import List

class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        order_map = defaultdict(lambda: -1)
        for index, i in enumerate(order):
            order_map[i] = index
        friends_order_map = defaultdict(lambda: -1)
        for i in friends:
            friends_order_map[i] = order_map[i]
        return sorted(friends, key = lambda x : friends_order_map[x])
