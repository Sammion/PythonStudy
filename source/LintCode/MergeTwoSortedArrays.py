class Solution:
    """
    @param: A: sorted integer array A
    @param: B: sorted integer array B
    @return: A new sorted integer array
    """

    def mergeSortedArray(self, A, B):
        # write your code here
        la = len(A)
        lb = len(B)
        if la == 0 or lb == 0:
            return None
        if A[la - 1] <= B[0]:
            return A + B
        elif B[lb - 1] <= A[0]:
            return B + A
        c = []
        i, j = 0, 0
        while i < la and j < lb:
            if A[i] <= B[j]:
                c.append(A[i])
                i += 1
            else:
                c.append(B[j])
                j += 1
        if i != la:
            c = c + A[i:]
        if j != lb:
            c = c + B[j:]
        return c
