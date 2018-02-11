"""

Given an array and a value, remove all occurrences of that value in place and return the new length.

The order of elements can be changed, and the elements after the new length don't matter.

给定一个数组和一个值，在原地删除与值相同的数字，返回新数组的长度。

元素的顺序可以改变，并且对新的数组不会有影响。

"""


class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """

    def removeElement(self, A, elem):
        # write your code here
        l = len(A)
        i, j = 0, 0
        while j < l:

            if A[j] != elem:
                A[i] = A[j]
                i += 1
            j += 1
        return i
