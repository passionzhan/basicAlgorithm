'''
sort algorithm, such as quicksort  bubble sort
by zhan 2018/11/29
'''


import random
import timeit


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


def heapSort(listA,):
    '''
    堆排序，自己实现，建堆过程不完整，只把最大/最小值移到了根节点
    :param listA:
    :return:
    '''
    # 完全二叉树叶子结点树 < 总结点数的/2
    def buildminheap(A, offset=0):
        if offset == len(A) - 1:
            return A

        # 从叶子结点开始递归向上，把最小值移动到根节点
        addNode = False
        tmpV = float('inf')
        if len(A[offset:]) % 2 == 0:
            A.append(tmpV)
            addNode = True

        endIdx = (len(A) - offset - 2) // 2 + offset
        for i in range(len(A) - 1, endIdx - 1, -2):
            minV = A[i]
            minIdx = i
            parentIdx = (i - offset - 1) // 2 + offset
            while parentIdx >= offset:
                left = (parentIdx - offset) * 2 + 1 + offset
                right = (parentIdx - offset) * 2 + 2 + offset
                if A[left] < minV:
                    minV = A[left]
                    minIdx = left
                if A[right] < minV:
                    minV = A[right]
                    minIdx = right
                if A[parentIdx] > minV:
                    A[parentIdx], A[minIdx] = A[minIdx], A[parentIdx]
                    minIdx = parentIdx
                parentIdx = (parentIdx - offset - 1) // 2 + offset

        if addNode:
            A.pop()
        # print(A[offset:])

        return A

    if len(listA) <= 1:
        return listA

    for i in range(len(listA)):
        buildminheap(listA, i)

    return listA


def heapSort2(listA):
    '''
    堆排序，标准实现
    :param listA:
    :return:
    '''
    def heapify(A, rootIdx=0, end=None):
        '''
        堆调整
        :param A:
        :param rootIdx:
        :param end:
        :return:
        '''
        if end is None:
            end = len(A) - 1

        if rootIdx < end:
            maxV = A[rootIdx]
            maxIdx = rootIdx
            left = 2 * rootIdx + 1
            right = 2 * rootIdx + 2

            if left <= end and A[left] > maxV:
                maxV = A[left]
                maxIdx = left
            if right <= end and A[right] > maxV:
                maxV = A[right]
                maxIdx = right

            if A[rootIdx] < maxV:
                A[rootIdx], A[maxIdx] = A[maxIdx], A[rootIdx]
                heapify(A, maxIdx, end)

        return A

    def buildMaxHeap(A):
        '''
        构建最大堆
        :param A:
        :return:
        '''
        # 从非叶子点倒序开始调整
        # 全完二叉树，非叶子结点数目为 len(A) // 2(向下取整)
        for i in range(len(A) // 2 - 1, -1, -1):
            heapify(A, i)

    if len(listA) <= 1:
        return listA

    buildMaxHeap(listA)

    for i in range(0, len(listA) - 1):
        listA[0], listA[len(listA) - 1 - i] = listA[len(listA) - 1 - i], listA[0]
        heapify(listA, 0, len(listA) - 1 - i - 1)

    return listA


def countingSort(listA):
    '''
    计数排序
    :param listA:
    :return:
    '''

    if len(listA) <= 1:
        return listA

    minV, maxV = float('inf'), float('-inf')
    for i in range(len(listA)):
        minV = min(minV,listA[i])
        maxV = max(maxV,listA[i])

    counting = {}
    for i in range(len(listA)):
        counting[listA[i]] = counting.setdefault(listA[i],0) + 1

    rtnList = []
    for i in range(minV, maxV + 1,):
        while counting.setdefault(i,0) > 0:
            rtnList.append(i)
            counting[i] -= 1

    return rtnList

if __name__ == '__main__':
    # listA = [43, 61, 8, 3, 1, 43, 21, 32, 49, 23, 9, 33, 2, 5, 82, 14, 17, 1]
    random.seed(33)
    listA = [random.randint(0, 1000) for i in range(23)]
    # listA = [i for i in range(17)]
    # listA = [-i for i in range(17)]
    # listA = []
    # listA = [4, ]
    # listA = [4, 0.9]
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
    # print('start merge sort...')
    # print(mergeSort(listA))
    # print('merge sort finish')
    # endregion

    # region quick sort
    # print('start quick sort...')
    # print(quickSort(listA,)
    # print('quick sort finish!')
    # endregion

    # region 堆排序
    # print('start heap sort...')
    # print(heapSort(listA))
    # # t1 = timeit.timeit('heapSort(listA)',
    # #                    'import random; from __main__ import heapSort; random.seed(23);listA = [random.randint(0, 100000) for i in range(1000)]',
    # #                    number=100, )
    # # print(t1)
    # print('heap sort finish')
    #

    # random.seed(33)
    # listA = [random.randint(0, 42) for i in range(37)]
    # print(listA)
    print('start heapSort_2 sort...')
    # print(heapSort2(listA))
    t2 = timeit.timeit('heapSort2(listA)',
                       'import random; from __main__ import heapSort2; random.seed(23);listA = [random.randint(0, 1777) for i in range(50000)]',
                       number=1000,)
    print(t2)
    print('heap sort finish')
    # endregion
    #
    # random.seed(33)
    # listA = [random.randint(0, 42) for i in range(37)]
    # print(listA)
    print('start counting sort...')
    # print(countingSort(listA))
    t2 = timeit.timeit('countingSort(listA)',
                       'import random; from __main__ import countingSort; random.seed(23);listA = [random.randint(0, 1777) for i in range(50000)]',
                       number=1000,)
    print(t2)
    print('counting sort finish')
    # endregion