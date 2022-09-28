"""
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.
"""

#!CLOSE CALL cant handle "bb" input
def longestPalindrome(s: str) -> str:
    palindrome = s[0]
    for i in s:
        temp = i
        for j in range(s.index(i) + 1, len(s)):
            if temp == temp[::-1] and len(temp) > len(palindrome):
                palindrome = temp
            temp += s[j]
    return palindrome

test = "babad"
print(longestPalindrome(test))