class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        ud = 0
        lr = 0
        for c in s:
            if c == 'U':
                ud += 1
            elif c == 'D':
                ud -= 1
            elif c == 'L':
                lr -= 1
            elif c == 'R':
                lr += 1
        coordinates = set()
        for i in range(k):
            if (s[i] == 'U'):
                ud -= 1
            elif (s[i] == 'D'):
                ud += 1
            elif (s[i] == 'L'):
                lr += 1
            elif (s[i] == 'R'):
                lr -= 1
        coordinates.add((ud, lr))
        for i in range(k, len(s)):
            if (s[i] == 'U'):
                ud += 1
            elif (s[i] == 'D'):
                ud -= 1
            elif (s[i] == 'L'):
                lr -= 1
            elif (s[i] == 'R'):
                lr += 1
            if (s[i-k] == 'U'):
                ud -= 1
            elif (s[i-k] == 'D'):
                ud += 1
            elif (s[i-k] == 'L'):
                lr += 1
            elif (s[i-k] == 'R'):
                lr -= 1
            coordinates.add((ud, lr))
        return len(coordinates)
