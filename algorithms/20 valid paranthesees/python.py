"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""


#!FEILER, Klarer ikke {[]}
def isValid(s: str) -> bool:
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    
    correctly_closed = True
    
    i = 0
    while i in range(len(s)):
        if (len(s) == 1) or (len(s)%2!=0):                                             #String contains only one parantheeses
            correctly_closed = False
        elif (s[i] in closing) or (s[i] in opening and s[i+1] in opening):
            correctly_closed = False
        elif opening.index(s[i]) != closing.index(s[i + 1]):
            correctly_closed = False
        else:
            correctly_closed = True
        i+=2
    return correctly_closed

test = "()(){]"
print(isValid(test))
                
