/*
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.
*/

//!NOT WORKING
var isPalindrome = function(x) {
    return x.toString().split("").reverse().join("") == x.toString()
};