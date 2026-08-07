class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        moves = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set()

        def flood_island(r,c):
            if r < 0 or r > rows-1:
                return
            if c < 0 or c > cols-1:
                return
            if (r,c) in visited:
                return
            if grid[r][c] == "0":
                return

            visited.add((r,c))

            for dr, dc in moves:
                flood_island(r+dr, c+dc)

        # find the first island
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    count += 1
                    flood_island(r,c)

        return count
