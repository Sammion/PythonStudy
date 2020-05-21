"""

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。

不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。

"""


class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        # write your code here
        l = len(nums)
        p, q = 0, 1
        if l == 0:
            return 0
        while q < l:
            if nums[p] == nums[q]:
                q += 1
            else:
                p += 1
                nums[p] = nums[q]
                q += 1
        return p + 1


if __name__ == '__main__':
    s = Solution()
    nums = [-10, 0, 1, 2, 3]
    print(s.removeDuplicates(nums))
