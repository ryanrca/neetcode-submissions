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

        def bfs(r, c, visited):
            fences = 0
            q = deque()

            q.append((r,c))
            visited.add((r,c))

            while q:
                for i in range(len(q)):
                    r,c = q.popleft()

                    for dr, dc in moves:
                        if r+dr < 0 or r+dr > rows:
                            fences += 1
                            continue
                        if c+dc < 0 or c+dc > cols:
                            fences += 1
                            continue
                        if grid[r+dr][c+dc] == 0:
                            fences += 1
                            continue
                        if (r+dr,c+dc) in visited:
                            continue
                        q.append((r+dr, c+dc))
                        visited.add((r+dr, c+dc))
    

            return fences

        # find the first island (1)
        for r in range(rows+1):
            for c in range(cols+1):
                if grid[r][c] == 1:

                    # fences = dfs(r,c, visited)
                    fences = bfs(r,c, visited)
                    return fences
        return 0
