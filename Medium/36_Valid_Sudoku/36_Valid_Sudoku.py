class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        answer = True
        for i in range(9):
            answer &= self.check_row(list(filter(lambda x: x != '.', board[i])))
        for i in range(9):
            answer &= self.check_column(list(filter(lambda x: x != '.', [ board[index][i] for index in range(9) ])))
        for i in [1, 4, 7]:
            for j in [1, 4, 7]:
                target_list = self.generate_square_list(i, j, board)
                answer &= self.check_square(list(filter(lambda x: x != '.', target_list)))
        return answer

    def check_row(self, row: List[str]) -> bool:
        return len(row) == len(set(row))
    def check_column(self, column: List[str]) -> bool:
        return len(column) == len(set(column))
    def check_square(self, square: List[str]) -> bool:
        return len(square) == len(set(square))

    def generate_square_list(self, x: int, y: int, board: List[List[str]]) -> List[str]:
        answer = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                answer.append(board[x+i][y+j])
        return answer