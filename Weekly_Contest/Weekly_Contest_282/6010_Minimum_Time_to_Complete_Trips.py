class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        upper_bound, lower_bound = min(time)*totalTrips , 1
        while(lower_bound < upper_bound):
            mid = (lower_bound+upper_bound)//2
            if (sum([mid//t for t in time]) >= totalTrips):
                upper_bound = mid
            else:
                lower_bound = mid+1

        return lower_bound