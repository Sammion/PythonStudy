"""

For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

给定一个排序的整数数组（升序）和一个要查找的整数target，用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。

"""


class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        l = len(nums)
        if l == 0:
            return -1
        elif l == 1:
            return 0
        return self.bSearch(nums, 0, l - 1, target)

    def bSearch(self, nums, start, end, target):
        if start > end:
            return -1
        if target > nums[end]:
            return -1
        if target < nums[start]:
            return -1
        mid = int((start + end) / 2)
        if target == nums[mid] and target != nums[mid - 1]:
            return mid
        elif target <= nums[mid]:
            return self.bSearch(nums, start, mid - 1, target)
        else:
            return self.bSearch(nums, mid + 1, end, target)
