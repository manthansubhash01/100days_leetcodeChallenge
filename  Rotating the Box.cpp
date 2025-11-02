// 1861. Rotating the Box
// Medium
// Topics
// premium lock iconCompanies
// Hint

// You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

//     A stone '#'
//     A stationary obstacle '*'
//     Empty '.'

// The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

// It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

// Return an n x m matrix representing the box after the rotation described above.

 

// Example 1:

// Input: boxGrid = [["#",".","#"]]
// Output: [["."],
//          ["#"],
//          ["#"]]

// Example 2:

// Input: boxGrid = [["#",".","*","."],
//               ["#","#","*","."]]
// Output: [["#","."],
//          ["#","#"],
//          ["*","*"],
//          [".","."]]

// Example 3:

// Input: boxGrid = [["#","#","*",".","*","."],
//               ["#","#","#","*",".","."],
//               ["#","#","#",".","#","."]]
// Output: [[".","#","#"],
//          [".","#","#"],
//          ["#","#","*"],
//          ["#","*","."],
//          ["#",".","*"],
//          ["#",".","."]]

 

// Constraints:

//     m == boxGrid.length
//     n == boxGrid[i].length
//     1 <= m, n <= 500
//     boxGrid[i][j] is either '#', '*', or '.'.

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
        int m = box.size();      // rows
        int n = box[0].size();   // columns

        // Step 1: Apply gravity in each row (stones fall to the right)
        for (int i = 0; i < m; ++i) {
            int write = n - 1; // position where next stone should fall
            for (int j = n - 1; j >= 0; --j) {
                if (box[i][j] == '*') {
                    write = j - 1; // reset after obstacle
                } 
                else if (box[i][j] == '#') {
                    // Move stone to write position if needed
                    if (j != write) {
                        box[i][write] = '#';
                        box[i][j] = '.';
                    }
                    write--; // next stone will fall above
                }
            }
        }

        // Step 2: Rotate the box 90° clockwise
        vector<vector<char>> rotated(n, vector<char>(m));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                rotated[j][m - 1 - i] = box[i][j];
            }
        }

        return rotated;
    }
};
