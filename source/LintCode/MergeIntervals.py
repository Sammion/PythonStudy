"""

Given a collection of intervals, merge all overlapping intervals.

给出若干闭合区间，合并所有重叠的部分。

"""


class Solution:
    """
    @param: intervals: interval list.
    @return: A new interval list.
    """

    def merge(self, intervals):
        # write your code here

        res = []
        if intervals is None:
            return res
        intervals.sort(key=lambda x: x.start)
        length = len(intervals)
        for i in range(length):
            if res == []:
                res.append(intervals[i])
            else:
                size = len(res)
                if res[size-1].start <= intervals[i].start <= res[size-1].end:
                    res[size-1].end = max(intervals[i].end, res[size-1].end)
                else:
                    res.append(intervals[i])
        return res


