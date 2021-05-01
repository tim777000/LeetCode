class SeatManager:

    def __init__(self, n: int):
        self.seatsList = [i for i in range(1, n+1)]
        return None

    def reserve(self) -> int:
        seatNumber = heapq.heappop(self.seatsList)
        return seatNumber

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.seatsList, seatNumber)
        return None


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)