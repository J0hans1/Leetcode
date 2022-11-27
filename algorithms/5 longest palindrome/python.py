"""
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

#!CLOSE CALL cant handle "bb" input
def longestPalindrome(s: str) -> str:
    longest = ""
    current = ""
    for i in range(len(s)):
        j = i
        while j < len(s):
            current += s[j]
            j += 1
            if len(current) > len(longest) and current == current[::-1]:
                longest = current
        current = ""
    return longest

test = "babad"
print(longestPalindrome(test))