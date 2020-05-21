"""

For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.

对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回 -1。

"""


class Solution:
    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """

    def strStr(self, source, target):
        # write your code here
        if type(source) is not str or type(target) is not str:
            return -1
        ls = len(source)
        lt = len(target)
        if ls < lt or (ls == 0 and lt > 0):
            return -1
        if (lt == 0 and ls == 0) or lt == 0:
            return 0
        s, t = 0, 0
        while s <= ls - lt:
            t = 0
            tmp = s
            while t < lt:

                if target[t] == source[s]:
                    t += 1
                    s += 1
                else:
                    break
            s = tmp
            if t == lt:
                break
            if s == ls - lt:
                return -1
            s += 1
        return s


if __name__ == '__main__':
    s = Solution()
    A = "tartarget"
    B = "target"
    print(s.strStr(A, B))
