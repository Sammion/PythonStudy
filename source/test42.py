# @author：Sam
# @date:2018-01-05
# desc：练习快速排序
# 思想：通过一趟排序将待排记录分割成两个部分，
# 其中一部分记录关键字均比另一部分记录的关键字小，则可以分别对这两部分关键字继续排序，以达到整个序列有序的目的。
# 时间复杂度：O(nlogn),最坏的情况下为O(n^2)
# 空间复杂度：O(1)
# 稳定性:不稳定

def quick_sort(l, left, right):
    if left >= right:
        return l
    key = l[left]
    low = left
    high = right
    while left < right:
        while left < right and l[right] >= key:
            right -= 1
        l[left] = l[right]
        while left < right and l[left] <= key:
            left += 1
        l[right] = l[left]
    print('key: ', key,' ', l)
    l[right] = key

    quick_sort(l, low, left)
    quick_sort(l, left + 1, high)
    return l


if __name__ == '__main__':
    l = [33, 2, 34, 45, 23, 12, 11, 35, 54, 100, 64, 86]
    print('Before sort: ', l)
    print('After sort: ', quick_sort(l, 0, 11))
