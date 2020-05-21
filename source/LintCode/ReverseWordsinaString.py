"""

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

给定一个字符串，逐个翻转字符串中的每个单词。

"""


class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        s = s.strip()
        l = s.split(" ")
        if len(l) <= 1:
            return s
        s = ""
        for i in range(len(l) - 1, 0, -1):
            s = s + (str(l[i])) + " "
        s = s + str(l[0])
        return s


if __name__ == '__main__':
    s = Solution()
    string = 'Good morining Jack  '
    string = 'How are you?   '
    # string.strip()
    print(string.reverser())
    print(s.reverseWords(string))
