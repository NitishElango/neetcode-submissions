class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for i in range(len(board)):
            row_seen = set()
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if board[i][j] in row_seen:
                        return False
                    else:
                        row_seen.add(board[i][j])
        #check cols
        for i in range(len(board)):
            col_seen = set()
            for j in range(len(board[0])):
                if board[j][i] != ".":
                    if board[j][i] in col_seen:
                        return False
                    else:
                        col_seen.add(board[j][i])
        
        row,col = [0,3,6], [0,3,6]
        for r in row:
            for c in col:
                mini = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] != ".":
                            if board[i][j] in mini:
                                return False
                            else:
                                mini.add(board[i][j])
        return True

        
        #0 012
        #1 012
        #2 012

        #0 345
        #1 345
        #2 345

        #0 678
        #1 678
        #2 678


        return True



