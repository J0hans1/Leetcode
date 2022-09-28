"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""

def isPalindrome(x: int) -> bool:
    return str(x)[::-1] == str(x)

test = 121
print(isPalindrome(test))