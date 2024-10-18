import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = [0] * (len(nums1) + len(nums2))
        mark1 = 0
        mark2 = 0
        count = 0
        flag = True
        while flag:
            if not(len(nums1) == 0 or len(nums2) == 0):
                if nums1[mark1] < nums2[mark2]:
                    nums[count] = nums1[mark1]
                    mark1 += 1
                else:
                    nums[count] = nums2[mark2]
                    mark2 += 1
                count += 1
                remaining = len(nums) - count
                if mark1 >= len(nums1):
                    nums[count : count + remaining] = nums2[mark2 : mark2 + remaining]
                    flag = False
                if mark2 >= len(nums2):
                    nums[count : count + remaining] = nums1[mark1 : mark1 + remaining]
                    flag = False
                if count > len(nums):
                    flag = False
            else:
                nums = nums1 + nums2
                flag = False
        return statistics.median(nums)
