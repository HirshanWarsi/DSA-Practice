class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        area = 0

        for i in range(rows):
            for j in range(cols):
                h = grid[i][j]

                if h > 0:
                    # top + bottom
                    area += 2
                    up = grid[i-1][j] if i > 0 else 0
                    down = grid[i+1][j] if i < rows - 1 else 0
                    left = grid[i][j-1] if j > 0 else 0
                    right = grid[i][j+1] if j < cols - 1 else 0

                    area += max(h - up, 0)
                    area += max(h - down, 0)
                    area += max(h - left, 0)
                    area += max(h - right, 0)

        return area