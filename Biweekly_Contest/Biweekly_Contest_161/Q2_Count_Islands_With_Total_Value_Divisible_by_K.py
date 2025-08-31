class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        visitedList = [ [False] * len(grid[0]) for i in range(len(grid)) ]
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == 0 or visitedList[i][j] == True):
                    continue
                s = self.dfs(grid, visitedList, i, j)
                if (s != 0 and s % k == 0):
                    result += 1
        return result
                
    def dfs(self, grid: List[List[int]], visitedList: List[List[int]], i: int, j: int) -> int:
        if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or visitedList[i][j] == True or grid[i][j] == 0):
            return 0
        if (visitedList[i][j] == False):
            visitedList[i][j] = True
        return grid[i][j] + self.dfs(grid, visitedList, i+1, j) + self.dfs(grid, visitedList, i-1, j) + self.dfs(grid, visitedList, i, j+1) + self.dfs(grid, visitedList, i, j-1)
