import string
class Solution(object):
    def lengthOfLastWord(self, s):
        has_word_started = False
        letter_count = 0
        for i in range(len(s)):
            s_minus_i = len(s) - i - 1
            if s[s_minus_i] in list(string.ascii_letters):
                has_word_started = True
                letter_count += 1
            elif has_word_started:
                return letter_count
            if i == len(s) - 1:
                return letter_count
