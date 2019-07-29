'''
sort algorithm, such as quicksort  bubble sort
by zhan 2018/11/29
'''


import random


def bubbleSort(listA):
    '''
    bubble sort algorithm.
    :param listA:
    :return:
    '''
    for i in range(len(listA)):
        for j in range(len(listA) - i - 1):
            if listA[j] > listA[j + 1]:
                listA[j], listA[j + 1] = listA[j + 1], listA[j]

    return listA


def selectSort(listA):
    '''
    选择排序
    :param listA:待排序列表
    :return:
    '''
    if len(listA) <= 1:
        return listA

    for i in range(len(listA)):
        for j in range(i + 1, len(listA)):
            if listA[j] < listA[i]:
                listA[i], listA[j] = listA[j], listA[i]

    return listA


def insertSort(listA):
    '''
    插入排序
    :param listA:
    :return:
    '''
    if len(listA) <= 1:
        return listA

    for i in range(len(listA) - 1):
        curV = listA[i + 1]
        preIdx = i
        while (preIdx >= 0 and curV < listA[preIdx]):
            listA[preIdx + 1] = listA[preIdx]
            preIdx -= 1

        listA[preIdx + 1] = curV

    return listA


def shellSort(listA):
    '''
    希尔排序
    :param listA:
    :return:
    '''
    if len(listA) <= 1:
        return listA

    gap = len(listA) // 2

    while gap > 0:
        for i in range(gap, len(listA),):
            curV = listA[i]
            preIdx = i - gap
            while(preIdx >= 0 and curV < listA[preIdx]):
                listA[preIdx + gap] = listA[preIdx]
                preIdx -= gap

            listA[preIdx + gap] = curV

        gap = gap // 2

    return listA


def mergeSort(listA):
    '''
    归并排序
    :param listA:
    :return:
    '''

    def merge(a, b):
        rtnList = []
        aIdx = 0
        bIdx = 0
        for i in range(len(a) + len(b)):
            if aIdx >= len(a):
                rtnList.append(b[bIdx])
                bIdx += 1
            elif bIdx >= len(b):
                rtnList.append(a[aIdx])
                aIdx += 1
            elif a[aIdx] <= b[bIdx]:
                rtnList.append(a[aIdx])
                aIdx += 1
            else:
                rtnList.append(b[bIdx])
                bIdx += 1

        return rtnList

    if len(listA) <= 1:
        return listA

    mid = len(listA) // 2
    leftList = mergeSort(listA[0:mid])
    rightList = mergeSort(listA[mid:])
    rstList = merge(leftList, rightList)

    return rstList


def quickSort(listA, start=0, end=None):
    '''
    quicksort algorithm.
    :param listA:待排序数组
    :param start:起始索引
    :param end: 终止索引
    :return: 排好序的列表
    '''
    if end is None:
        end = len(listA)

    if start < end:
        baseV = listA[start]
        i, j = start, end
        while i < j:
            while i < j and listA[j] >= baseV:
                j = j - 1
            listA[i] = listA[j]

            while i < j and listA[i] <= baseV:
                i = i + 1
            listA[j] = listA[i]

        listA[i] = baseV

        quickSort(listA, start, i - 1)
        quickSort(listA, i + 1, end)
    return listA


if __name__ == '__main__':
    listA = [43, 61, 8, 3, 1, 43, 21, 32, 49, 23, 9, 33, 2, 5, 82, 14, 17, 1]
    listA = [random.randint(0, 500) for i in range(17)]
    listA = [i for i in range(17)]
    listA = [-i for i in range(17)]
    listA = []
    listA = [4, ]
    listA = [4, 0.9]
    print(listA)

    # region 冒泡排序
    # print('start bubble sort...')
    # print(bubbleSort(listA))
    # print('bubble sort finish')
    # endregion

    # region 选择排序
    # print('start select sort...')
    # print(selectSort(listA))
    # print('select sort finish')
    # endregion

    # region 插入排序
    # print('start insert sort...')
    # print(insertSort(listA))
    # print('insert sort finish')
    # endregion

    # region 希尔排序
    # print('start shell sort...')
    # print(shellSort(listA))
    # print('shell sort finish')
    # endregion

    # region 归并排序
    print('start merge sort...')
    print(mergeSort(listA))
    print('merge sort finish')
    # endregion

    # region quick sort
    # print('start quick sort...')
    # print(quickSort(listA,)
    # print('quick sort finish!')
    # endregion
