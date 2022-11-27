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