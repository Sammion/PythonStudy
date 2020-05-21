"""

Given a rotated sorted array, recover it to sorted array in-place.

给定一个旋转排序数组，在原地恢复其排序。

"""


class Solution:
    """
    @param: nums: An integer array
    @return: nothing
    """

    def recoverRotatedSortedArray(self, nums):
        # write your code here
        ln = len(nums)
        index = 0
        for i in range(ln-1):
            if (nums[i] > nums[i + 1]):
                index = i + 1
                break
        for i in range(int(index / 2)):
            tmp = nums[i]
            nums[i] = nums[index - 1 - i]
            nums[index - 1 - i] = tmp
        for i in range(int((ln - index) / 2)):
            tmp = nums[index + i]
            nums[index + i] = nums[ln - 1 - i]
            nums[ln - 1 - i] = tmp
        for i in range(int(ln / 2)):
            tmp = nums[i]
            nums[i] = nums[ln - 1 - i]
            nums[ln - 1 - i] = tmp
