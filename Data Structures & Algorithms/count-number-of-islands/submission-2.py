class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def is_in_bounds(i, j):
            return 0 <= i < rows and 0 <= j < cols
        
        def dfs(i, j):
            if not is_in_bounds(i, j):
                return
            if grid[i][j] == "0":
                return
            if (i, j) in visited:
                return
            visited.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0" or \
                   ((i, j) in visited):
                    continue
        
                count += 1
                dfs(i, j)

        return count 
        