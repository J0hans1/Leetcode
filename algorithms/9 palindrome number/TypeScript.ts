/*
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.
*/

//*SUCCESS
function isPalindrome(x: number): boolean {
    return x.toString().split("").reverse().join("") == x.toString();
};