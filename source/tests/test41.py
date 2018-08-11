# @author：Sam
# @date:2018-01-05
# desc：练习冒泡排序
# 思想：重复走访过要排序的序列，一次比较两个元素，如果他们的顺序错误就将他们进行交换，一次冒上来的是最小的，其次是第二小。
# 时间复杂度：O(n^2)
# 空间复杂度:O(1)

def bubble_sort(l):
    count = len(l)
    for i in range(count):
        for j in range(i + 1, count):
            if l[j] < l[i]:
                l[j], l[i] = l[i], l[j]
        print(l)
    return l


if __name__ == '__main__':
    l = [1, 2, 34, 45, 23, 12, 11, 35, 54, 100, 64, 86]
    print('Before sort: ', l)
    print('After sort: ', bubble_sort(l))
