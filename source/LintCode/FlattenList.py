"""

Given a list, each element in the list can be a list or integer. flatten it into a simply list with integers.

给定一个列表，该列表中的每个要素要么是个列表，要么是整数。将其变成一个只包含整数的简单列表。

"""


class Solution(object):
    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        self.res = []
        if nestedList is None:
            return []
        if type(nestedList) == int:
            self.res.append(nestedList)
            return self.res

        for i in nestedList:
            if type(i) == int:
                self.res.append(i)
            else:
                self.recursion(i)
        return self.res

    def recursion(self, l):
        if l is None:
            return
        for i in l:
            if type(i) == int:
                self.res.append(i)
            else:
                self.recursion(i)


if __name__ == '__main__':
    i = 100
    s = Solution()
    print(type(i) == int)
    nl = [1, [1, 2, [3, 4, 5]], [7, 8], [9, 10]]
    print(s.flatten(nl))
