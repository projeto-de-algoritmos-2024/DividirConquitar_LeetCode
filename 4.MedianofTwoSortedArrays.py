from typing import List

from typing import List


class Solution:
    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = j = 0
        temp = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1

        while i < len(nums1):
            temp.append(nums1[i])
            i += 1

        while j < len(nums2):
            temp.append(nums2[j])
            j += 1

        return temp

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = self.merge(nums1, nums2)
        n = len(nums)

        if n % 2 == 0:
            median = (nums[n // 2 - 1] + nums[n // 2]) / 2
        else:
            median = nums[n // 2]

        return float("{0:.5f}".format(median))


solution = Solution()
print(solution.findMedianSortedArrays([2, 2, 4, 4], [2, 2, 2, 4, 4]))
print(solution.findMedianSortedArrays([1, 3], [2]))
print(solution.findMedianSortedArrays([1, 2], [3, 4]))
print(solution.findMedianSortedArrays([3], [-2, -1]))
