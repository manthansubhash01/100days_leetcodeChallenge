# 3211. Generate Binary Strings Without Adjacent Zeros
##################################################################################################
'''
You are given a positive integer n.
A binary string x is valid if all substrings of x of length 2 contain at least one "1".
Return all valid strings with length n, in any order.


Example 1:

Input: n = 3

Output: ["010","011","101","110","111"]

Explanation:

The valid strings of length 3 are: "010", "011", "101", "110", and "111".

Example 2:

Input: n = 1

Output: ["0","1"]

Explanation:

The valid strings of length 1 are: "0" and "1".


Constraints:

    1 <= n <= 18

'''
##################################################################################################

class Solution:
    def validStrings(self, n: int) -> List[str]:
        lst = []
        for i in range(2**n):
            s = ""
            while i > 0 :
                s += str(i%2)
                i //= 2
            num = s[::-1]
            ans = ((n-len(num)) * "0") + num
            if "00" not in ans:
                lst.append(ans)
        return lst