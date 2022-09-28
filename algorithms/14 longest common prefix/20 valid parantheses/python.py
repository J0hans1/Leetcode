"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


#!LIST IMPORT PROBLEM
def longestCommonPrefix(strs: List[str]) -> str:
    prefix = ""
    temp = ""
    for i in strs[0]:
        for j in strs:
            if temp + i not in j:
                if len(prefix) > len(temp):
                    prefix = temp
                break
            temp += i
        temp = ""
    return prefix

test = ["flower","flow","flight"]
print(longestCommonPrefix(str(test)))