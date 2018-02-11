"""

The words are same rotate words if rotate the word to the right by loop, and get another. Count how many different rotate word sets in dictionary.

E.g. picture and turepic are same rotate words.

给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)
python 2 能实现这个功能

"""


class Solution:
    """
    @param: str: An array of char
    @param: offset: An integer
    @return: nothing
    """

    def rotateString(self, str, offset):
        # write your code here
        if str is None or len(str) == 0 or offset == 0:
            return str
        l = len(str)
        offset = offset % l
        for i in range(offset):
            t = str.pop()
            str.insert(0,t)
        # return str
if __name__ == '__main__':
    s= Solution()
    print(s.rotateString('abcdefg',3))