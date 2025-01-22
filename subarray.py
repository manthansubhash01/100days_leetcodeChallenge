# Minimum size subarray sum 
# level Medium 
'''Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

 

Constraints:

    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104 '''

def minSubArrayLen(target, nums) : 
    n = len(nums)
    pre = [0]*(n)
    pre[0] = nums[0]
    for i in range(1,n):
        pre[i] = pre[i-1] + nums[i]
    l,r = 0,1
    length = n
    while r < n:
        if l == 0 and pre[r] >= target  :
            if pre[l] <  target : 
                length = r + 1
            else :
                length = 1
            l += 1
        elif pre[r] - pre[l] >= target  and length > r - l :
            length = r - l
            l += 1
        elif pre[r] - pre[l] < target :
            r += 1
        elif pre[r] - pre[l] >= target :
            l += 1
    if pre[-1] < target :
        return 0
    else:
        return length