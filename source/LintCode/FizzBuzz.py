"""

Given number n. Print number from 1 to n. But:

    when number is divided by 3, print "fizz".
    when number is divided by 5, print "buzz".
    when number is divided by both 3 and 5, print "fizz buzz".


给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：

    如果这个数被3整除，打印fizz.
    如果这个数被5整除，打印buzz.
    如果这个数能同时被3和5整除，打印fizz buzz.

"""


class Solution:
    """
    @param: n: An integer
    @return: A list of strings.
    """

    def fizzBuzz(self, n):
        # write your code here
        l = []
        if n <= 0:
            return l
        elif n < 3:
            return list(range(1, n + 1))

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                l.append("fizz buzz")
            elif i % 3 == 0:
                l.append("fizz")
            elif i % 5 == 0:
                l.append("buzz")
            else:
                l.append(str(i))
        return l
