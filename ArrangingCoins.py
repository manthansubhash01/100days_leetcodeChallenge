# 441. Arranging Coins
###########################################################################################
'''
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:

Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:

Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

 

Constraints:

    1 <= n <= 2^31 - 1
'''
###########################################################################################

class Solution:
    def arrangeCoins(self, n: int) -> int:
        def num_coin(num):
            return (num*(num+1))//2
        def arrange(n):
            low,high = 0,n
            ans = 0
            while low <= high:
                mid = (low+high)//2
                if num_coin(mid) <= n:
                    if ans < mid:
                        ans = mid
                    low = mid+1
                elif num_coin(mid) > n:
                    high = mid-1
            return ans
        return arrange(n)