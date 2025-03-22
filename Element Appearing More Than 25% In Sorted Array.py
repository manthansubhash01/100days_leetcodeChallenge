# 1287. Element Appearing More Than 25% In Sorted Array
######################################################################
'''
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:

Input: arr = [1,1]
Output: 1

 

Constraints:

    1 <= arr.length <= 10^4
    0 <= arr[i] <= 10^5
'''
######################################################################

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        def binary_search(arr,target):
            n = len(arr)
            low,high = 0,n-1
            ans = [-1,-1]
            while low <= high:
                mid = (low+high)//2
                if arr[mid] == target:
                    ans[0] = mid
                    high = mid-1
                elif arr[mid] > target:
                    high = mid-1
                else:
                    low = mid+1
            low,high = 0,n-1
            while low <= high:
                mid = (low+high)//2
                if arr[mid] == target:
                    ans[1] = mid
                    low = mid+1
                elif arr[mid] > target:
                    high = mid-1
                else:
                    low = mid+1
            return ans
        def find_special_integer(arr):
            n = len(arr)
            for i in arr:
                ans = binary_search(arr,i)
                if ((ans[1]-ans[0]+1)/n)*100 > 25:
                    return i
        return find_special_integer(arr)