// 459. Repeated Substring Pattern
// Solved
// Easy
// Topics
// premium lock iconCompanies

// Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

// Example 1:

// Input: s = "abab"
// Output: true
// Explanation: It is the substring "ab" twice.

// Example 2:

// Input: s = "aba"
// Output: false

// Example 3:

// Input: s = "abcabcabcabc"
// Output: true
// Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

 

// Constraints:

//     1 <= s.length <= 104
//     s consists of lowercase English letters.



class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        string doubled = s + s;
        string modified = doubled.substr(1, doubled.size() - 2);
        return modified.find(s) != string::npos;
    }
};
