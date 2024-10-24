class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(sum(int(item) for item in str(num)) for num in nums)
