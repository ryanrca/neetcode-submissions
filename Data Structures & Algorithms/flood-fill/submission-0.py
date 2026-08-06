class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows = len(image) - 1
        cols = len(image[0]) - 1
        moves = [[0,1],[1,0],[0,-1],[-1,0]]
        visited = set()

        start_color = image[sr][sc]

        def flood(r, c, image, color, visited):

            if r < 0 or r > rows:
                return
            if c < 0 or c > cols:
                return
            if image[r][c] != start_color:
                return

            if (r,c) in visited:
                return

            if image[r][c] == start_color:
                image[r][c] = color
                visited.add((r,c))

            for dr, dc in moves:
                flood(r+dr, c+dc, image, color, visited)

            return

        flood(sr,sc, image, color, visited)
        return image
