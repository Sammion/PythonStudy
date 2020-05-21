def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1


def changeStr(str, index, char):
    if index > len(str):
        return str
    else:
        # print(str[index])
        str = list(str)
        str[index] = char
        # str.join(char)
        return str


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


def sqrt(self, x):
    begin = 0
    end = x
    if x == 0: return 0
    if x == 1: return 1
    while True:
        mid = (begin + end) / 2
        if mid ** 2 == x:
            return mid
        # x处于[begin,end]中间的一个数
        # 如果mid**2 < x，且(mid+1) **2 >x，则mid为最接近于x的平方根
        if mid ** 2 < x and (mid + 1) ** 2 > x:
            return mid
        elif mid ** 2 < x:
            begin = mid
            end = end
            continue
        else:
            begin = begin
            end = mid
            continue


# 求两个数的平均值
def average(a, b):
    return (a + b) / 2.0


def improve(guess, x):
    return average(guess, x / guess)


# 控制迭代次数
def good_enough(guess, x):
    d = abs(guess * guess - x)
    return (d < 0.001)


# 求开方函数
def square_root(guess, x):
    while (not good_enough(guess, x)):
        guess = improve(guess, x)
    return guess


#
def my_sqrt(x):
    r = square_root(1, x)
    return r


def MySqt(x):
    if x == 0 or x == 1:
        return x
    else:
        tmp = (1.0 + (x / 1.0)) / 2.0
        while abs(tmp ** 2 - x) > 0.001:
            tmp = 1.0 / 2.0 * (tmp + x / tmp)
        return tmp


# 链表节点定义
class Node(object):
    def __init__(self, x, n=None):
        self.val = x
        self.next = n


# 链表反转实现
def reversal(head, newhead):
    if head is None:
        return
    if head.next is None:
        newhead = head
    else:
        newhead = reversal(head.next, newhead)
        head.next.next, head.next = head, None
    return newhead


class TreeNode:
    def __init__(self, v, l=None, r=None):
        self.val = v
        self.lchild = l
        self.rchild = r


import copy


def PreOrder(bt):
    l = []
    if bt.val is None:
        return
    p = bt
    results = []
    while (p is not None or len(l) != 0):
        while (p is not None):
            l.append(p)
            results.append(p.val)
            p = p.lchild
        if len(l) != 0:
            p = l.pop()

            p = p.rchild
    return results


def PreOrder2(bt):
    l = []
    if bt.val is None:
        return
    p = copy.deepcopy(bt)
    while True:
        if p is not None:
            l.append(p)
        if p.rchild is not None:
            l.append()


if __name__ == '__main__':
    str = 'star@ust'
    str = changeStr(str, 4, 'd')
    print(str)
    for i in fab(10):
        print(i)
    print(my_sqrt(13))
    print(MySqt(13))
    a1 = TreeNode('G')
    a2 = TreeNode('H')
    b1 = TreeNode('D', a1, a2)
    b2 = TreeNode('B', b1)
    c1 = TreeNode('I')
    c2 = TreeNode('E', None, c1)
    c3 = TreeNode('F')
    c4 = TreeNode('C', c2, c3)
    bt = TreeNode('A', b2, c4)
    print(PreOrder(bt))
