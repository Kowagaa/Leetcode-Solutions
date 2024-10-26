class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                count += 1
        return count
