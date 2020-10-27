class Solution {
public:
    int containVirus(vector<vector<int>>& grid) {
        int ans = 0;
        while (true) {
            int walls = process(grid);
            if (walls == 0) break; // No more walls to build
            ans += walls;
        }
        return ans;
    }
private:
    int process(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        // cnt is max area to be affected by a single virus region; ans is corresponding walls
        int cnt = 0, ans = 0, color = -1, row = -1, col = -1;
        // visited virus as 1, visited 0 using different color to indicate being affected by different virus
        vector<vector<int>> visited(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && visited[i][j] == 0) {
                    int walls = 0, area = dfs(grid, visited, i, j, color, walls);
                    if (area > cnt) {
                        ans = walls;
                        cnt = area;
                        row = i;
                        col = j;
                    }
                    color--;
                }
            }
        }
        // set this virus region inactive
        buildWall(grid, row, col);
        // propagate other virus by 1 step
        visited = vector<vector<int>>(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 && visited[i][j] == 0)
                    spread(grid, visited, i, j);
            }
        }
        return ans;
    }
    int dfs(vector<vector<int>>& grid, vector<vector<int>>& visited, int row, int col, int color, int& walls) {
        int m = grid.size(), n = grid[0].size(), ans = 0;
        if (row < 0 || row >= m || col < 0 || col >= n) return 0;
        if (grid[row][col] == 0) {
            walls++;
            if (visited[row][col] == color) return 0;
            visited[row][col] = color;
            return 1;
        }
        // grid[row][col] could be -1, inactive virus
        if (visited[row][col] == 1 || grid[row][col] != 1) return 0;
        visited[row][col] = 1;
        vector<int> dir = {-1, 0, 1, 0, -1};
        for (int i = 0; i < 4; i++)
            ans += dfs(grid, visited, row+dir[i], col+dir[i+1], color, walls);
        return ans;
    }
    void buildWall(vector<vector<int>>& grid, int row, int col) {
        int m = grid.size(), n = grid[0].size();
        if (row < 0 || row >= m || col < 0 || col >= n || grid[row][col] != 1) return;
        grid[row][col] = -1; //set inactive
        vector<int> dir = {-1, 0, 1, 0, -1};
        for (int i = 0; i < 4; i++)
            buildWall(grid, row+dir[i], col+dir[i+1]);
    }
    void spread(vector<vector<int>>& grid, vector<vector<int>>& visited, int row, int col) {
        int m = grid.size(), n = grid[0].size();
        if (row < 0 || row >= m || col < 0 || col >= n || visited[row][col] == 1) return;
        if (grid[row][col] == 0) {
            grid[row][col] = 1;
            visited[row][col] = 1;
        }
        else if (grid[row][col] == 1) {
           visited[row][col] = 1;
           vector<int> dir = {-1, 0, 1, 0, -1};
           for (int i = 0; i < 4; i++)
               spread(grid, visited, row+dir[i], col+dir[i+1]);
        }
    }
};