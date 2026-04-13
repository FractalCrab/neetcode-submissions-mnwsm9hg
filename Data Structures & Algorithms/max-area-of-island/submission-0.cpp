class Solution {
public:
    int dfs(vector<vector<int>>& grid, int row, int col) { 
        int rows = grid.size(); 
        int cols = grid[0].size(); 
        int max_reach = 0;
        if (row < 0 || col < 0 || row >= rows || col >= cols || grid[row][col] == 0) 
            return max_reach; 
        
        grid[row][col] = 0; 
        
        vector<pair<int,int>> dirs = {{1,0},{-1,0},{0,1},{0,-1}}; 
        max_reach = 1;
        for (auto &d : dirs) {
            max_reach += dfs(grid, row + d.first, col + d.second); 
            
        }
        // cout << "max = " << max_reach << " ";
        return max_reach;
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int rows = grid.size(); 
        int cols = grid[0].size(); 
        int count = 0; 
        for (int r = 0; r < rows; r++) 
            for (int c = 0; c < cols; c++) 
                if (grid[r][c] == 1) { 
                    count = max(count, dfs(grid, r, c)); 
                }

        return count;
    }


};
