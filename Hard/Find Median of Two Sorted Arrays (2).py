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
        if len(nums) % 2 == 0: return (nums[len(nums) // 2] + nums[len(nums) // 2 - 1])/2
        else: return nums[len(nums) // 2]
#This version of the code doesnt use the statistics module, its slower (7ms compared to 6ms) but it works without the need of the module
