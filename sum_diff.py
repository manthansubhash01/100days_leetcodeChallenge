# 2574. Left and Right Sum Differences
'''Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:
    answer.length == nums.length.
    answer[i] = |leftSum[i] - rightSum[i]|.

Where:
    leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
    rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.

Return the array answer.

Example 1:

Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

Example 2:

Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].

Constraints:

    1 <= nums.length <= 1000
    1 <= nums[i] <= 10^5'''

class Solution:
    def leftRightDifference(self, nums) :
        n = len(nums)
        pre = [0] * n
        pre[0] = nums[0]
        for i in range(1,n):
            pre[i] = pre[i-1] + nums[i]
        suf = [0] * n
        suf[0] = suf[-1]
        for i in range(-1,-n-1,-1):
            suf[i] = suf[i+1] + nums[i]
        answer = []
        if n == 1:
            answer.append(0)
        else :
            for i in range(n-1):
                if i == 0 :
                    answer.append(suf[i+1])
                elif i < n-1 :
                    answer.append(abs(pre[i-1]-suf[i+1]))
            answer.append(pre[n-2])
        return answer