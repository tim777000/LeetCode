class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size_of_matrix = len(matrix)
        for i in range(size_of_matrix):
            for j in range(i, size_of_matrix):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in matrix:
            i.reverse()

