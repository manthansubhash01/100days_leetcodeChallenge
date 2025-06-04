# 110. Balanced Binary Tree
#############################################################################
'''
Given a binary tree, determine if it is

.

 

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:

Input: root = []
Output: true

 

Constraints:

    The number of nodes in the tree is in the range [0, 5000].
    -10^4 <= Node.val <= 10^4
'''
#############################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if not node:
                return 0, True

            left_height, left_balanced = check(node.left)
            right_height, right_balanced = check(node.right)

            current_height = 1 + max(left_height, right_height)
            is_balanced = (
                left_balanced and
                right_balanced and
                abs(left_height - right_height) <= 1
            )

            return current_height, is_balanced

        return check(root)[1]