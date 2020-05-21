"""

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are zero-based.

给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。

你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围是 0 到 n-1。

"""


class Solution:
    """
    @param: numbers: An array of Integer
    @param: target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here
        d = dict()
        for i in range(len(numbers)):
            d[target - numbers[i]] = i
        res = list()
        for j in range(len(numbers)):
            if numbers[j] in d.keys():
                res.append(min(j, d[numbers[j]]))
                res.append(max(j, d[numbers[j]]))
                return res


if __name__ == '__main__':
    n = [1,0,-1]
    t = -1
    s = Solution()
    print(s.twoSum(n, t))
