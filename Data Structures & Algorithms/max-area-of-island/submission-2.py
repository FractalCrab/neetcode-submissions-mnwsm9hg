class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    continue

                grid[i][j] = 0
                stack = [(i, j)]
                area = 0

                while stack:
                    r, c = stack.pop()
                    area += 1
                    for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
                            grid[nr][nc] = 0
                            stack.append((nr, nc))

                max_area = max(max_area, area)

        return max_area