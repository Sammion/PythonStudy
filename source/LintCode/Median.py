"""

Given a unsorted array with integers, find the median of it.

A median is the middle number of the array after it is sorted.

If there are even numbers in the array, return the N/2-th number after sorted.


给定一个未排序的整数数组，找到其中位数。

中位数是排序后数组的中间值，如果数组的个数是偶数个，则返回排序后数组的第N/2个数。

"""

class Solution:
    """
    @param: : A list of integers
    @return: An integer denotes the middle number of the array
    """

    def median(self, nums):
        # write your code here
        if len(nums) == 0:
            return None
        if len(nums) <= 2:
            return nums[0]
        else:
            return self.quicksort(nums, 0, len(nums) - 1)

    def quicksort(self, nums, start, end):
        pivot = nums[start]
        l = len(nums)
        i = start
        j = end
        if start >= end:
            return nums[start]
        while i < j:
            while i < end and nums[i] <= pivot:
                    i += 1
            while j > start and nums[j] >= pivot:
                    j -= 1

            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                break
        if pivot > nums[i]:
            nums[start], nums[i] = nums[i], nums[start]
        if i == int((l - 1) / 2):
            return nums[i]
        elif i < int((l - 1) / 2):
            return self.quicksort(nums, i + 1, end)
        else:
            return self.quicksort(nums, start, i - 1)


if __name__ == '__main__':
    nums = [-1, -2, -3, -100, -1, -50]
    s = Solution()
    print(s.median(nums))
