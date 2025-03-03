'''
912. Sort an Array
Solved
Medium
Topics
Companies

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).

Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.

 

Constraints:

    1 <= nums.length <= 5 * 104
    -5 * 104 <= nums[i] <= 5 * 104
'''

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l1,l2):
            n=len(l1)
            m=len(l2)
            result = []
            i,j = 0,0
            while i < n and j < m:
                if l1[i] <= l2[j]:
                    result.append(l1[i])
                    i += 1
                else:
                    result.append(l2[j])
                    j += 1
            while i < n:
                result.append(l1[i])
                i += 1
            while j < m:
                result.append(l2[j])
                j += 1
            return result
        def merge_sort(arr):
            if len(arr)==1:
                return arr 
            else:
                mid=len(arr)//2
            s1=merge_sort(arr[0:mid])
            s2=merge_sort(arr[mid:])
            s=merge(s1,s2)
            return s
        return merge_sort(nums)
