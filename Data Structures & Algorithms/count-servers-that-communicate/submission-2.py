class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        servers = 0

        #pre process:
        row_count = [0] * rows
        col_count = [0] * cols

        sum = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:      # for every server
                    if (row_count[r] > 1 or col_count[c] > 1):   # is there more than 1 in the r or c
                        servers += 1

        return servers
