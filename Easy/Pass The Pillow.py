class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        current = 0
        while time > 0:
            for i in range(n - 1):
                current += 1
                time -= 1
                if time <= 0:
                    return current + 1
            for i in range(n - 1):
                current -= 1
                time -= 1
                if time <= 0:
                    return current + 1
