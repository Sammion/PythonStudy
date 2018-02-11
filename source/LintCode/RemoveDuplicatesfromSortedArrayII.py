"""

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].

跟进“删除重复数字”：

如果可以允许出现两次重复将如何处理？
"""

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        # write your code here
        l = len(nums)
        if l <= 2:
            return l

        i, q = 2, 2
        while i < l:
            if nums[i] != nums[q - 2]:
                nums[q] = nums[i]
                q += 1
            i += 1
        return q


if __name__ == '__main__':
    s = Solution()
    nums = [-10, 0, 1, 2, 3]
    print(s.removeDuplicates(nums))
