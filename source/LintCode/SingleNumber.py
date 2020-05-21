"""

Given 2*n + 1 numbers, every numbers occurs twice except one, find it.

给出2*n + 1 个的数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。

"""

class Solution:
    """
    @param: A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        # write your code here
        ans = 0
        for i in A:
            ans ^= i
        return ans

