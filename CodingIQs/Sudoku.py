class Solution(object):
    def isValidSudoku(self, board):
        # declaring sets:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in rows:
            for c in cols:
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3, c//3]):
                    return False
                # if not add cols, rows, and squares
                cols[c].add[board[r][c]]
                rows[r].add[board[r][c]]
                squares[r//3, c//3].add[board[r][c]]
        return True
