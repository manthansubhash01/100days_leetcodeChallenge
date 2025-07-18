// 994. Rotting Oranges

// You are given an m x n grid where each cell can have one of three values:

//     0 representing an empty cell,
//     1 representing a fresh orange, or
//     2 representing a rotten orange.

// Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

// Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

// Example 1:

// Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
// Output: 4

// Example 2:

// Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
// Output: -1
// Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

// Example 3:

// Input: grid = [[0,2]]
// Output: 0
// Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

 

// Constraints:

//     m == grid.length
//     n == grid[i].length
//     1 <= m, n <= 10
//     grid[i][j] is 0, 1, or 2.



class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        vector<int> dx = {1, -1, 0, 0};
        vector<int> dy = {0, 0, 1, -1};
        vector<vector<bool>> visited(n, vector<bool>(m, false));
        queue<pair<int,pair<int,int>>> q;

        int time = 0;

        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(grid[i][j] == 2){
                    q.push({0,{i,j}});
                }
            }
        }

        while(!q.empty()){
            pair<int,pair<int,int>> x = q.front();
            q.pop();

            for(int i = 0; i < 4; i++){
                int a = dx[i] + x.second.first;
                int b = dy[i] + x.second.second;

                if(a >= 0 && b >= 0 && a < n && b < m && !visited[a][b] && grid[a][b] == 1){
                    visited[a][b] = true;
                    q.push({x.first+1,{a,b}});
                    time = max(time,x.first+1);
                }
            }
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(grid[i][j] == 1 && !visited[i][j]) return -1;
            }
        }

        return time;
    }
};