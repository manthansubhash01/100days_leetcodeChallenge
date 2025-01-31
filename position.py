# 34 First and Last position of element in sorted array 
'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

 

Constraints:

    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    nums is a non-decreasing array.
    -10^9 <= target <= 10^9'''

class Solution:
    def searchRange(self, nums, target):
        n = len(nums)
        start = -1 
        low = 0 
        high = n-1 
        while low <= high :
            mid = (low + high) // 2
            if nums[mid] == target :
                start = mid 
                high = mid - 1
            elif nums[mid] > target :
                high = mid - 1
            else :
                low = mid + 1
        end = -1
        low = 0 
        high = n-1 
        while low <= high :
            mid = (low + high) // 2
            if nums[mid] == target :
                end = mid 
                low = mid + 1
            elif nums[mid] > target :
                high = mid - 1
            else :
                low = mid + 1
        return (start,end)