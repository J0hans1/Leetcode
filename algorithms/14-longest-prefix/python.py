class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortest = min(strs, key=len)
        for i in shortest:
            if all(word.startswith(prefix + i) for word in strs):
                prefix += i
        return prefix