class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        moves = [[0,1], [1,0], [0,-1], [-1,0]]
        rows = len(grid) - 1
        cols = len(grid[0]) - 1

        def dfs(r, c, visited) -> int:
            
            fences = 0

            if r < 0 or r > rows:
                return 1
            if c < 0 or c > cols:
                return 1

            if grid[r][c] == 0:
                return 1
            if (r,c) in visited:
                return 0

            visited.add((r,c))

            for dr, dc in moves:
                fences += dfs(r+dr, c+dc, visited)
            return fences

        # find the first island (1)
        for r in range(rows+1):
            for c in range(cols+1):
                if grid[r][c] == 1:

                    fences = dfs(r,c, visited)
                    return fences
                
        return 0
