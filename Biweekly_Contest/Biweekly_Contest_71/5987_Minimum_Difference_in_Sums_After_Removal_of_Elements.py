class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)//3

        left_part = [-num for num in nums[0:n]]
        mid_part = nums[n:2*n]
        right_part = nums[2*n:3*n]

        heapq.heapify(left_part)
        heapq.heapify(right_part)
        min_left_part = [0]*(n+1)
        max_right_part = [0]*(n+1)
        min_left_part[0] = -sum(left_part)
        max_right_part[n] = sum(right_part)

        for i in range(0, n):
            heapq.heappush(left_part, -mid_part[i])
            left_pop_value = -heapq.heappop(left_part)
            min_left_part[i+1] = min_left_part[i] + mid_part[i] - left_pop_value

            heapq.heappush(right_part, mid_part[(n-1)-i])
            right_pop_value = heapq.heappop(right_part)
            max_right_part[(n-1)-i] = max_right_part[(n-1)-i+1] + mid_part[(n-1)-i] - right_pop_value

        answer = inf
        for i in range(0, n+1):
            answer = min(answer, min_left_part[i] - max_right_part[i])

        return answer

