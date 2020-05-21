"""

Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find it.

给定一个整型数组，找出主元素，它在数组中的出现次数严格大于数组元素个数的二分之一。

"""


class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """

    def majorityNumber(self, nums):
        # write your code here
        if nums is None:
            return
        d = dict()
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        tmp = 0
        res = 0
        for j in d.keys():
            if d[j] > tmp:
                tmp = d[j]
                res = j
        return res
    # 第二种方法
    def secondMethod(self, nums):
        ln = len(nums)
        cnt, res = 0, None
        for i in nums:
            if cnt == 0:
                res = i
                cnt = 1
            elif i == res:
                cnt += 1
            else:
                cnt -= 1
        return res
