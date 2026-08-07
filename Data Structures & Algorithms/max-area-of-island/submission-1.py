class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_size = 0
        rows = len(grid)
        cols = len(grid[0])
        moves = [[0,1], [1,0], [0,-1], [-1,0]]

        visited = set()

        def flood_island(r,c):
            if r < 0 or r > rows-1:
                return 0
            if c < 0 or c > cols-1:
                return 0
            if (r,c) in visited:
                return 0
            if grid[r][c] == 0:
                return 0

            visited.add((r,c))
            size = 1

            for dr, dc in moves:
                size += flood_island(r+dr, c+dc)
            return size

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    size = flood_island(r,c)
                    max_size = max(size, max_size)

        return max_size
