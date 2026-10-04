class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        
        def is_in_bounds(i, j):
            return 0 <= i < rows and 0 <= j < cols
        
        def dfs(i, j):
            if not is_in_bounds(i, j):
                return 0
            if grid[i][j] == 0:
                return 0
            if (i, j) in visited:
                return 0
            visited.add((i, j))
            
            return (
                    1
                    + dfs(i + 1, j)
                    + dfs(i - 1, j)
                    + dfs(i, j + 1)
                    + dfs(i, j - 1)
                )


        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0 or \
                   ((i, j) in visited):
                    continue
        
                max_area = max(dfs(i, j), max_area)

        return max_area  