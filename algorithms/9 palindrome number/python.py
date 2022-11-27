"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""

#*SUCCESS
def isPalindrome(self, x: int) -> bool:
    s = str(x)
    return s==s[::-1]

#*FOLLOW UP
def isPalindromeNoStr(x: int) -> bool:
    return x == reverse(x)

def reverse(x: int) -> int:
    if x < 0:                               #   if x is negative
        return -x                           #   return the positive version of x because it is never equal to x
    reversed = 0                            #   reversed will be the reversed version of x
    while x != 0:                           #   while there still are digits
        reversed = reversed * 10 + x % 10   #   you move the reversed number to the left and add the digit
        x //= 10                            #   you target the next digit by moving to the right
    return reversed                         #   return the reversed number 



