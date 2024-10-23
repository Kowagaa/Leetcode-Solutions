class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = [item for item in s if item in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"]
        s = ""
        for i in range(len(s2)):
            s += s2[i].lower()
        for i in range(len(s)//2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True
