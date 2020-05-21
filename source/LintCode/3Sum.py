"""
57. 3Sum


Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Notice

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.



给出一个有n个整数的数组S，在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。
注意事项

在三元组(a, b, c)，要求a <= b <= c。

结果不能包含重复的三元组。

"""


class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        # write your code here
        ln = len(numbers)
        d = dict()
        for i in range(ln):
            d[0 - numbers[i]] = i
        res = list()
        for target in d.keys():
            tres = self.twoSum(numbers, target, d[target])
            res.append(tres)
        return res

    # 求两个数的组合等于目标值，需要出除其本身
    def twoSum(self, numbers, target, t_id):
        # write your code here
        d = dict()
        for i in range(len(numbers)):
            d[target - numbers[i]] = i
        res = list()
        l_res = list()
        for j in range(len(numbers)):
            if numbers[j] in d.keys() and j != t_id:
                res.append(numbers[j])
                res.append(numbers[d[numbers[j]]])
                res.append(numbers[t_id])
                res.sort()
                l_res.append(res)
            if j == len(numbers) - 1 and not res:
                return False
        return l_res


if __name__ == '__main__':
    n = [-2, -3, 5, -1, -4, 5, -11, 7, 1, 2, 3, 4, -7, -1, -2, -3, -4, -5]
    n1 = [-1, 1, 0]
    s = Solution()
    res = s.threeSum(n1)
    print(res)
