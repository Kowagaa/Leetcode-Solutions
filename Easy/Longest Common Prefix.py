class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortest = 200
        for i in range(len(strs)):
            if len(strs[i]) < shortest:
                shortest = len(strs[i])
        for i in range(shortest):
            for j in range(len(strs) - 1):
                if not(strs[j][i] == strs[j + 1][i]):
                    return prefix
            prefix += strs[0][i]
        return prefix
