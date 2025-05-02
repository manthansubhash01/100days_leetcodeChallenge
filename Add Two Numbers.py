# 2. Add Two Numbers
#############################################################
'''
Editorial
Editorial
Solutions
Solutions
Submissions
Submissions
Code
Testcase
Test Result
Test Result
2. Add Two Numbers
Solved
Medium
Topics
Companies

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

 

Constraints:

    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
'''
#############################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def addNumber(first, second):
            new_head = ListNode(0)
            current = new_head
            carry = 0
            f = first 
            s = second 
            while f or s or carry:
                if f :
                    val1 = f.val
                else:
                    val1 = 0
                if s :
                    val2 = s.val
                else:
                    val2 = 0
                total = val1+val2+carry
                carry = total//10
                digit = total%10
                current.next = ListNode(digit)
                current = current.next
                if f:
                    f = f.next
                if s:
                    s = s.next
            return new_head.next
        return addNumber(l1, l2)