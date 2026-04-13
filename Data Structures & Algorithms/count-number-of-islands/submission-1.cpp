class Solution {
public:
    void dfs(vector<vector<char>>& grid, int row, int col) {
        int rows = grid.size();
        int cols = grid[0].size();

        if (row < 0 || col < 0 || row >= rows || col >= cols || grid[row][col] == '0')
            return;

        grid[row][col] = '0';

        vector<pair<int,int>> dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        for (auto &d : dirs)
            dfs(grid, row + d.first, col + d.second);
    }
    int numIslands(vector<vector<char>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        int numIslands = 0;

        for (int row = 0; row < rows; ++row){
            for (int col = 0; col < cols; ++col)
                if (grid[row][col] == '1'){
                    dfs(grid, row, col);
                    numIslands ++;
                }
        }
        return numIslands;
    }
};
