class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dup_squares = [{} for _ in range(9)] # 9 hash tables representing 9 squares

        ROWS = len(board)
        COLS = len(board[0])

        # check rows:
        for r in range(ROWS):
            dup_rows = {}
            for c in range(COLS):
                val = board[r][c]
                if val == '.':
                    continue
                # add the row vals:
                dup_rows[val] = 1 + dup_rows.get(val, 0)
                if dup_rows[val] > 1:
                    return False
                
                # add the square vals:
                index = (r // 3) * 3 + (c // 3)
                dup_squares[index][val] = 1 + dup_squares[index].get(val, 0)
                if dup_squares[index][val] > 1:
                    return False

        # check cols:
        for c in range(COLS):
            dup_cols = {}
            for r in range(ROWS):
                val = board[r][c]
                if val == '.':
                    continue
                dup_cols[val] = 1 + dup_cols.get(val, 0)
                if dup_cols[val] > 1:
                    return False

        return True