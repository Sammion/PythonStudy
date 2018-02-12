"""

Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1], calculate B WITHOUT divide operation.


给定一个整数数组A。

定义B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]， 计算B的时候请不要使用除法。

"""

class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        # write your code here
        l = len(nums)
        resDisct = dict()
        left = 1
        for i in range(l):
            resDisct[i] = 1
        for i in range(l):
            resDisct[i] *= left
            left *= nums[i]
        right = 1
        for j in range(l-1,-1,-1):
            resDisct[j] *= right
            right *= nums[j]
        resList = list()
        for i in range(l):
            resList.append(resDisct[i])
        return resList