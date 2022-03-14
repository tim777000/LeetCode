class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapping_dict = { index:element for index, element in enumerate(mapping) }
        nums_tuple = []
        for num in nums:
            mapping_num = ""
            for d in str(num):
                mapping_num += str(mapping_dict[int(d)])
            nums_tuple.append((int(mapping_num), num))
        answer = sorted(nums_tuple, key=lambda n: n[0])
        return [ a[1] for a in answer]