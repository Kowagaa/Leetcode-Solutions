class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = [0, 0]
        for i in range(len(nums)):
            for j in range(0, i - 1):
                if nums[i] + nums[j] == target:
                    out = [i, j]
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    out = [i, j]
        return out
