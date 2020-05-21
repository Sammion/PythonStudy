# @author：Sam
# @date:2018-01-04
# desc：练习插入排序
# 插入排序的基本操作就是将一个数据插入到已经排好序的有序数据中，从而得到一个新的、个数加一的有序数据，
# 算法适用于少量数据的排序，时间复杂度为O(n^2)。
# 是稳定的排序方法。
# 插入算法把要排序的数组分成两部分：第一部分包含了这个数组的所有元素，但将最后一个元素除外（让数组多一个空间才有插入的位置），
# 而第二部分就只包含这一个元素（即待插入元素）。
# 在第一部分排序完成后，再将这个最后元素插入到已排好序的第一部分中。

def insert_sort(lists):
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1], lists[j] = lists[j], key
                # lists[j + 1] = lists[j]
                # lists[j] = key
            j -= 1
    return lists


if __name__ == '__main__':
    list = [1, 2, 34, 45, 23, 12, 11, 35, 54, 100, 64, 86, 29]
    print('Before sort: ', list)
    print('After sort: ', insert_sort(list))
