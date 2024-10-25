import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return True if float(int(math.log(n,4)) == math.log(n,4)) else False
        return False
