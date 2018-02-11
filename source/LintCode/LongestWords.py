"""
Given a dictionary, find all of the longest words in the dictionary.

给一个词典，找出其中所有最长的单词。
"""


class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """

    def longestWords(self, dictionary):
        # write your code here
        tmp = len(dictionary[0])
        res = []
        for i in dictionary:
            if len(i) > tmp:
                tmp = len(i)
                res = [i]
            elif len(i) == tmp:
                res.append(i)
        return res
