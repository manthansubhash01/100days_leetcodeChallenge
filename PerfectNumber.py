# 507. Perfect Number
######################################################################
'''
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

 

Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:

Input: num = 7
Output: false

 

Constraints:

    1 <= num <= 10^8
'''
######################################################################

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        x=0
        k = int(num**(0.5))
        for i in range(1,k+1):
            if num%i==0:
                x+=i
                x+=(num//i)
        x -= num
        if x==num:
            return True
        return False