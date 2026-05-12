class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            row_set = set()
            for j in range(len(board[0])):
                if board[i][j].isdigit():
                    if board[i][j] in row_set:
                        return False
                    else:
                        row_set.add(board[i][j])

        for j in range(len(board[0])):
            col_set = set()
            for i in range(len(board)):
                if board[i][j].isdigit():
                    if board[i][j] in col_set:
                        return False
                    else:
                        col_set.add(board[i][j])
        row = 0
        col = 0
        while True:
            if row >= 8:
                if col >= 8:
                    return True
                else:
                    row = 0
                    col += 3
            grid_set = set()
            for i in range(row, row+3):
                for j in range(col, col + 3):
                    if i == 8 and j == 8:
                        return True
                    if board[i][j].isdigit():
                        if board[i][j] in grid_set:
                            return False
                        else:
                            grid_set.add(board[i][j])
            row +=3
        return True