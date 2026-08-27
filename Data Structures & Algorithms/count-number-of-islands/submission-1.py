class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ret = 0
        seen = set()
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        ROWS = len(grid)
        COLS = len(grid[0])

        def flood_island(r, c):
            if r < 0 or r >= ROWS:
                return
            if c < 0 or c >= COLS:
                return
            if (r,c) in seen:
                return
            if grid[r][c] == "0":
                return
            
            seen.add((r,c))

            for i in range(len(dr)):
                flood_island(r+dr[i], c+dc[i])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    if (r,c) not in seen:
                        ret += 1
                        flood_island(r,c)

        return ret
        