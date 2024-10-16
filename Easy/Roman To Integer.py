class Solution(object):
    def romanToInt(self, s):
        int_list = [self.numeral_to_int(s[0])]
        prev = int_list[0]
        count = 1
        for i in range(1, len(s)):
            if self.numeral_to_int(s[i]) == prev:
                int_list[i - count] += self.numeral_to_int(s[i])
                count += 1
                prev = self.numeral_to_int(s[i])
            else:
                int_list.append(self.numeral_to_int(s[i]))
                prev = self.numeral_to_int(s[i])
        for i in range(len(int_list) - 1):
            if int_list[i] < int_list[i + 1]:
                int_list[i + 1] -= int_list[i]
                int_list[i] = 0
        return sum(int_list) 
    def numeral_to_int(self, numeral):
        if numeral == 'M':
            return 1000
        if numeral == 'D':
            return 500
        if numeral == 'C':
            return 100
        if numeral == 'L':
            return 50
        if numeral == 'X':
            return 10
        if numeral == 'V':
            return 5
        if numeral == 'I':
            return 1
