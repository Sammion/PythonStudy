'''
Compare two strings A and B, determine whether A contains all of the characters in B.

The characters in string A and B are all Upper Case letters.

比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是 大写字母
'''


class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: if string A contains all of the characters in B return true else return false
    """

    def compareStrings(self, A, B):
        # write your code here
        if len(A) < len(B):
            return False
        elif len(B) == 0:
            return True
        m = dict()
        for i in A:
            if i in m:
                m[i] = m[i] + 1
            else:
                m[i] = 1
        for j in B:
            if j in m:
                m[j] -= 1
            else:
                return False
        for v in m.values():
            if v < 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    A = "ABC"
    B = "A"
    print(s.compareStrings(A, B))
