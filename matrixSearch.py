# 74. Search a 2D Matrix
#############################################################
'''You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.


Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -10^4 <= matrix[i][j], target <= 10^4'''
#############################################################

class Solution:
    def searchMatrix(self, matrix, target) :
        def find(lst,target,i,j) :
            low ,high = i,j
            col = len(lst[0])
            while low <= high :
                mid = (low + high) // 2
                r = mid // col
                c = mid % col
                if lst[r][c] == target :
                    return True 
                elif lst[r][c] <  target :
                    low = mid + 1
                else :
                    high = mid - 1 
            return False 
        n = len(matrix)
        m = len(matrix[0])
        result = find(matrix,target,0,n * m - 1)
        return result