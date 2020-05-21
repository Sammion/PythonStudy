# @author：Sam
# @date:2018-01-04
# desc：练习shell排序
# 希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
# 希尔排序是非稳定排序算法。
# 该方法因DL．Shell于1959年提出而得名。
# 希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；
# 随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。

def shell_sort(l):
    count = len(l)
    step = 2
    group = int(count / step)
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = l[j]
                while k >= 0:
                    if l[k] > key:
                        l[k + group], l[k] = l[k], key
                    k -= group
                j += group
        #
        group = int(group/step)
    return l


if __name__ == '__main__':
    l = [1, 2, 34, 45, 23, 12, 11, 35, 54, 100, 64, 86]
    print('Before sort: ', l)
    print('After sort: ', shell_sort(l))
