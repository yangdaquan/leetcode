
'''
1 冒泡排序
'''


def BubbleSort_1(l):
    length = len(l)
    for i in range(length):
        for j in range(length-1-i):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


def BubbleSort_2(l):
    length = len(l)
    for i in range(length):
        for j in range(i+1, length):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l


'''
2 选择排序
'''


def select_sort(l):
    length = len(l)
    for i in range(length):
        min = i
        for j in range(i+1, length):
            if l[min] > l[j]:
                min = j
        l[min], l[i] = l[i], l[min]
    return l

'''
3 插入排序
'''


def InsertSort(l):
    length = len(l)
    for i in range(1, length):
        current = l[i]
        j = i - 1

        while j >= 0:
            if l[j] > current:
                l[j+1] = l[j]
                l[j] = current
            j -= 1

    return l

'''
4 希尔排序
'''

def sheelSort(l):
    length = len(l)
    gap = round(length / 2)

    while gap > 0:
        for i in range(gap, length):
            # 每个步长进行插入排序
            current = l[i]
            j = i

            while j >= gap and l[j - gap] > current:
                l[j] = l[j - gap]
                j -= gap

            l[j] = current

        gap = round(gap / 2)

    return l


'''
5 归并排序
'''


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(l):
    if len(l) <= 1:
        return l
    num = len(l) // 2
    left = merge_sort(l[:num])
    right = merge_sort(l[num:])
    return merge(left, right)


'''
6 快速排序
'''


def quick_sort_1(l):
    less = []
    pivotlist = []
    more = []

    if len(l) <= 1:
        return list
    else:
        pivot = l[0]
        for i in l:
            if i < pivot:
                less.append(i)
                print('less', less)
            elif i > pivot:
                more.append(i)
                print('more', more)
            else:
                pivotlist.append(i)
                print('pivotlist', pivotlist)

        less = quick_sort_1(less)
        more = quick_sort_1(more)
        return less + pivotlist + more


def quick_sort_2(l):
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        return quick_sort_2([x for x in l if x < pivot]) +\
               [pivot] +\
               quick_sort_2([x for x in l if x > pivot])


if __name__ == '__main__':

    l = [20, 3, 5, 15, 2, 26, 4, 7, 54, 8, 19]

    print('BubbleSort_1(l)', BubbleSort_1(l))
    print('BubbleSort_2(l)', BubbleSort_2(l))
    print('select_sort(l)', select_sort(l))
    print('InsertSort(l)', InsertSort(l))
    print('sheelSort(l)', sheelSort(l))
    print('merge_sort(l)', merge_sort(l))
    print('quick_sort_1(l)', quick_sort_1(l))
    print('quick_sort_2(l)', quick_sort_2(l))
    print('quick_sort_2(l)', quick_sort_2(l))



