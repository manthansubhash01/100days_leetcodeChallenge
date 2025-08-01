// 25. Reverse Nodes in k-Group
// Solved
// Hard
// Topics
// premium lock iconCompanies

// Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

// k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

// You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

// Example 1:

// Input: head = [1,2,3,4,5], k = 2
// Output: [2,1,4,3,5]

// Example 2:

// Input: head = [1,2,3,4,5], k = 3
// Output: [3,2,1,4,5]

 

// Constraints:

//     The number of nodes in the list is n.
//     1 <= k <= n <= 5000
//     0 <= Node.val <= 1000

 

// Follow-up: Can you solve the problem in O(1) extra memory space?






class Solution {
public:
    // Function to reverse a portion of the list between start and end (exclusive of end)
    ListNode* reverse(ListNode* start, ListNode* end) {
        ListNode* prev = end;
        while (start != end) {
            ListNode* tmp = start->next;
            start->next = prev;
            prev = start;
            start = tmp;
        }
        return prev;
    }

    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) return head;

        // Dummy node simplifies the head handling
        ListNode dummy(0);
        dummy.next = head;

        ListNode* groupPrev = &dummy;

        while (true) {
            ListNode* kth = groupPrev;
            // Find the kth node from groupPrev
            for (int i = 0; i < k && kth; ++i) {
                kth = kth->next;
            }
            if (!kth) break; // Not enough nodes left to reverse

            ListNode* groupNext = kth->next;
            ListNode* groupStart = groupPrev->next;

            // Reverse the group
            ListNode* newGroupHead = reverse(groupStart, groupNext);

            // Connect previous part to reversed group
            groupPrev->next = newGroupHead;
            groupStart->next = groupNext;

            // Move groupPrev to the end of the reversed group
            groupPrev = groupStart;
        }

        return dummy.next;
    }
};
