class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        flag = True
        while flag:
            n2 = list(str(n))
            prod = 1
            for i in range(len(n2)):
                prod = prod * int(n2[i])
            if prod % t == 0:
                flag = False
            n += 1
        return n - 1
