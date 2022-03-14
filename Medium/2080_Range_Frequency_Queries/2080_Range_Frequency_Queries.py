class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.frequency_dict = dict()
        for (index, value) in enumerate(arr):
            if value in self.frequency_dict:
                self.frequency_dict[value].append(index)
            else:
                self.frequency_dict[value] = [index]

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.frequency_dict:
            return 0
        min_index = bisect.bisect(self.frequency_dict[value], left)
        max_index = bisect.bisect(self.frequency_dict[value], right)
        return max_index - min_index

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)