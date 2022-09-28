'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

#FUNGERER FOR ARRAYS MEN IKKE LINKED LISTS
def addTwoNumbersB(l1, l2):
    lx = [str(x) for x in l1[::-1]]
    ly = [str(y) for y in l2[::-1]]
    result = int("".join(lx)) + int("".join(ly))     
    return [int(x) for x in [*(str(result)[::-1])]]

l1 = [2,4,3]
l2 = [5,6,4]

print(addTwoNumbersB(l1, l2))