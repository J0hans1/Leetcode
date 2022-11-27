"""
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.
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