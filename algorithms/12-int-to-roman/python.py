"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= num <= 3999
"""
class Solution:
    table = {
        1 : "I",
        4 : "IV",
        5 : "V",
        9 : "IX",
        10 : "X",
        40 : "XL",
        50 : "L",
        90 : "XC",
        100 : "C",
        400 : "CD",
        500 : "D",
        900 : "CM",
        1000 : "M"
    }

    def intToRoman(self, num: int) -> str:
        roman = ""
        stringNum = str(num)[::-1]
        for i in range(len(stringNum)):
            roman = self.desipher(int(stringNum[i]), 10**i) + roman
        return roman

    def desipher(self, sipher : int, position : int):
        for j in self.table:
            if j == position:
                if position * sipher == j:
                    return self.table[j]
                elif sipher < 4:
                    return (self.table[j] * sipher)
                # double symbol for 4, 40 and 400
                elif sipher == 4:
                    return self.table[4 * position]
                # double symbol for 9, 90, 900
                elif sipher == 9:
                    return self.table[9 * position]
                # 5 =< sipher < 9
                elif sipher < 9:
                    return self.table[5 * position] + (self.table[position] * (sipher - 5))
                else:
                    continue    