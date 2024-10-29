class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = list(str(-x))[::-1]
            x2 = ""
            for i in range(len(x)):
                x2 += x[i]
            x = -int(x2)
            if x < -2** 31:
                return 0
        else:
            x = list(str(x))[::-1]
            x2 = ""
            for i in range(len(x)):
                x2 += x[i]
            x = int(x2)
            if x > 2** 31 - 1:
                return 0
        return x
