class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #checks rows and cols
        for i in range(len(board)):
            rowset = set()
            colset = set()
            for j in range(len(board[0])):
                if board[i][j] in rowset:
                    return False
                if board[j][i] in colset:
                    return False
                if board[i][j] not in rowset and board[i][j].isnumeric():
                    rowset.add(board[i][j])
                if board[j][i] not in colset and board[j][i].isnumeric():
                    colset.add(board[j][i])
        #checks 3x3 grids
        r,c = 0, 0
        while r < len(board) and c < len(board[0]):
            mset = set()
            for i in range(r, r + 3):
                for j in range(c, c+3):
                    if board[i][j] in mset:
                        return False
                    else:
                        if board[i][j].isnumeric():
                            mset.add(board[i][j])
            c+=3
            if c >= len(board[0]):
                c = 0
                r+=3
        return True

        