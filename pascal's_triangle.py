# Pascal's Triangle 
'''Given an integer numRows, return the first numRows of Pascal's triangle.
Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

 

Constraints:

    1 <= numRows <= 30'''

import math
class Solution:
    def generate(self, numRows: int):
        lst = []
        for i in range(numRows):
            row = []
            x = math.factorial(i)
            for j in range(i+1):
                y = math.factorial(j)
                z = math.factorial(i - j)
                row.append(x//(y*z))
            lst.append(row)
        return lst