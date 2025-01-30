# 345. Reverse Vowels of a String 
'''Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

    1 <= s.length <= 3 * 10^5
    s consist of printable ASCII characters.'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        lst = list(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        l,r = 0,n-1
        while l <= r :
            if lst[l] in vowels and lst[r] in vowels :
                lst[l],lst[r] = lst[r],lst[l]
                l += 1
                r -= 1
            elif lst[l] in vowels and lst[r] not in vowels :
                r -= 1
            elif lst[l] not in vowels and lst[r] in vowels :
                l += 1
            elif lst[l] not in vowels and lst[r] not in vowels :
                l += 1
                r -= 1
        return "".join(lst)