# Solution 1
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            check = set()
            for i in range(9):
                if board[row][i] == '.':
                    continue
                if board[row][i] in check:
                    return False
                check.add(board[row][i])
            
        for col in range(9):
            check = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in check:
                    return False
                check.add(board[i][col])

        for squares in range(9):
            check = set()
            for i in range(3):
                for j in range(3):
                    row = (squares//3) * 3 + i
                    col = (squares%3) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in check:
                        return False
                    check.add(board[row][col])
        return True


valsud = Solution()
valsud.isValidSudoku([
 ["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]])
