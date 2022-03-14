class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        check_matrix = [0]*(n+1)
        answer = True
        for row in matrix:
            for index in range(0, n+1):
                check_matrix[index] = 0
            for row_element in row:
                if (check_matrix[row_element] == 1):
                    answer = False
                    break
                else:
                    check_matrix[row_element] = 1
        if (answer == False):
            return answer
        for column_index in range(0, n):
            for index in range(0, n+1):
                check_matrix[index] = 0
            for row in matrix:
                if (check_matrix[row[column_index]] == 1):
                    answer = False
                    break
                else:
                    check_matrix[row[column_index]] = 1
        return answer