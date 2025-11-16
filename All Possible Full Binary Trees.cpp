// 894. All Possible Full Binary Trees
// Solved
// Medium
// Topics
// premium lock iconCompanies

// Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

// Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

// A full binary tree is a binary tree where each node has exactly 0 or 2 children.

 

// Example 1:

// Input: n = 7
// Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]

// Example 2:

// Input: n = 3
// Output: [[0,0,0]]

 

// Constraints:

//     1 <= n <= 20

class Solution {
public:
    unordered_map<int, vector<TreeNode*>> memo;

    vector<TreeNode*> allPossibleFBT(int n) {
        if (n % 2 == 0) return {};
        
        if (memo.count(n)) return memo[n];
        
        vector<TreeNode*> result;
        if (n == 1) {
            result.push_back(new TreeNode(0));
            return memo[n] = result;
        }
        for (int leftCount = 1; leftCount < n; leftCount += 2) {
            int rightCount = n - 1 - leftCount;

            vector<TreeNode*> leftTrees = allPossibleFBT(leftCount);
            vector<TreeNode*> rightTrees = allPossibleFBT(rightCount);

            for (auto left : leftTrees) {
                for (auto right : rightTrees) {
                    TreeNode* root = new TreeNode(0);
                    root->left = left;
                    root->right = right;
                    result.push_back(root);
                }
            }
        }

        return memo[n] = result;
    }
};
