class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        answer = True
        sorted_asteroids = sorted(asteroids)
        for index, asteroid in enumerate(sorted_asteroids):
            if mass >= asteroid:
                mass += asteroid
            else:
                answer = False

        return answer
