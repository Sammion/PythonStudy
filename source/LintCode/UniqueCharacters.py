"""

Implement an algorithm to determine if a string has all unique characters.

实现一个算法确定字符串中的字符是否均唯一出现

"""


class Solution:
    """
    @param: str: A string
    @return: a boolean
    """

    def isUnique(self, str):
        # write your code here
        if str is None:
            return False
        s = set(str)
        if len(str) == len(s):
            return True
        else:
            return False

    def isUnique2(self, str):
        # write your code here
        if str is None:
            return False
        elif len(str) > 128:
            return False
        m = dict()
        for i in range(256):
            m[i] = 0
        for j in str:
            asc = ord(j)
            print(asc)
            m[asc] = m[asc] + 1
            if m[asc] > 1:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    l = 'abgiadhafuih'
    print(s.isUnique2(l))
