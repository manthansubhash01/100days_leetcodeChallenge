# 123. Best Time to Buy and Sell Stock III
###########################################################################################################
'''
Accepted
Accepted
Editorial
Editorial
Solutions
Solutions
Submissions
Submissions
Code
Testcase
Testcase
Test Result
123. Best Time to Buy and Sell Stock III
Solved
Hard
Topics
Companies

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

 

Constraints:

    1 <= prices.length <= 10^5
    0 <= prices[i] <= 10^5
'''
###########################################################################################################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        left_profit = [0] * n
        min_price = prices[0]
        for i in range(1, n):
            min_price = min(min_price, prices[i])
            left_profit[i] = max(left_profit[i - 1], prices[i] - min_price)
        max_price = prices[-1]
        right_profit = [0] * n
        for i in range(n - 2, -1, -1):
            max_price = max(max_price, prices[i])
            right_profit[i] = max(right_profit[i + 1], max_price - prices[i])
        max_total_profit = 0
        for i in range(n):
            max_total_profit = max(max_total_profit, left_profit[i] + right_profit[i])
        return max_total_profit