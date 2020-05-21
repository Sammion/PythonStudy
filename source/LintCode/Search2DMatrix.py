"""

Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

写出一个高效的算法来搜索 m × n矩阵中的值。

这个矩阵具有以下特性：

    每行中的整数从左到右是排序的。
    每行的第一个数大于上一行的最后一个整数。

"""


class Solution:
    """
    @param: matrix: matrix, a list of lists of integers
    @param: target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if matrix is None:
            return False
        m = len(matrix)
        if m ==0:
            return False
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == target:
                    return True
        return False
