class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        prev_pos = [(0,0)]
        tick = 0
        for i in range(3, len(distance)):
            if i >= 3 and distance[i] >= distance[i - 2] and distance[i - 1] <= distance[i - 3]: return True
            if i >= 4 and distance[i - 1] == distance[i - 3] and distance[i - 2] <= distance[i] + distance[i - 4]: return True
            if i >= 5 and distance[i - 2] >= distance[i - 4] and distance[i - 3] - distance[i - 5] <= distance[i - 1] <= distance[i - 3] and distance[i] >= distance[i - 2] - distance[i - 4]: return True
        return False
