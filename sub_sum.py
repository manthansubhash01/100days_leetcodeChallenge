#1588. Sum of All Odd Length Subarrays
##########################################################################
'''Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
A subarray is a contiguous subsequence of the array.

Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.

Example 3:

Input: arr = [10,11,12]
Output: 66

Constraints:

    1 <= arr.length <= 100
    1 <= arr[i] <= 1000'''
##########################################################################

class Solution:
    def sumOddLengthSubarrays(self, arr):
        n = len(arr)
        total = 0
        pre = [0] * n
        pre[0] = arr[0]
        for i in range(1,n):
            pre[i] = pre[i-1] + arr[i]
        total = sum(arr)
        if n >= 3 :
            for i in range(3,n+1,2):
                for j in range(i-1,n):
                    if j == i-1:
                        total += pre[j]
                    else:
                        total += (pre[j]-pre[j-i])
        return total