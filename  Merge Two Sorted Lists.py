# 21. Merge Two Sorted Lists
#######################################################################################
'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

 

Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
'''
#######################################################################################

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def Merge(head1, head2):
            dummy = ListNode(-1)
            tail = dummy
            while head1 and head2:
                if head1.val <= head2.val:
                    tail.next = head1
                    head1 = head1.next
                else:
                    tail.next = head2
                    head2 = head2.next
                tail = tail.next
            if head1:
                tail.next = head1
            if head2:
                tail.next = head2
            return dummy.next
        return Merge(list1, list2)