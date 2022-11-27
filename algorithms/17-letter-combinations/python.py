class Solution:
    mapping = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5" : "jkl",
        "6" : "mno",
        "7" : "pqrs",
        "8" : "tuv",
        "9" : "wxyz"
    }
    
    def letterCombinations(self, digits: str):
        result = []
        for i in digits:
            result = [x + y for x in result or [''] for y in self.mapping[i]] 
        return result