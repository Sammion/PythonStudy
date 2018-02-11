"""

Given two sorted integer arrays A and B, merge B into A as one sorted array.

合并两个排序的整数数组A和B变成一个新的数组。

"""


class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """

    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        m = m - 1
        n = n - 1
        l = m + n + 1
        while m >= 0 or n >= 0:
            if m < 0:
                A[l] = B[n]
                l -= 1
                n -= 1
                continue
            if n < 0:
                A[l] = A[m]
                l -= 1
                m -= 1
                continue
            if A[m] > B[n]:
                A[l] = A[m]
                l -= 1
                m -= 1
            else:
                A[l] = B[n]
                l -= 1
                n -= 1
        return A


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3, 0, 0]
    B = [4, 5]
    print(s.mergeSortedArray(A, 3, B, 2))
