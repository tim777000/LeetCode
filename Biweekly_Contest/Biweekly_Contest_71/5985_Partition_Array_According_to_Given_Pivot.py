class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left_list = []
        right_list = []
        pivot_count = 0
        for num in nums:
            if num < pivot:
                left_list.append(num)
            elif num > pivot:
                right_list.append(num)
            else:
                pivot_count += 1

        return left_list + [pivot]*pivot_count + right_list