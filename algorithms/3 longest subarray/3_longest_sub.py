'''
Given a string s, find the length of the longest substring without repeating characters.
'''

#*SUCCESS
def lengthOfLongestSubstring(s: str) -> int:
    result = 0
    for i in range(len(s)):
        temp = str(s[i])
        for j in range(i + 1, len(s)):
            if s[j] not in temp:
                temp += s[j]
            else:
                break
        if len(temp) > result:
            result = len(temp)
    return result

test = "abcabcbb"
print(lengthOfLongestSubstring(test))


