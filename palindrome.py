# 125. Valid Palindrome 
'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

 

Constraints:

    1 <= s.length <= 2 * 105
    s consists only of printable ASCII characters. '''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst = [x.lower() for x in s if ((ord(x) > 64 and ord(x) < 91) or (ord(x) > 96 and ord(x) < 123) or (ord(x) > 47 and ord(x) < 58))]
        new_s = "".join(lst)
        n = len(new_s)
        l,r = 0,n-1 
        if new_s == "" :
            return True
        else :
            Palindrome = True
            while l < r :
                if new_s[l] != new_s[r] :
                    Palindrome = False
                    break 
                else :
                    l += 1
                    r -= 1
            return Palindrome