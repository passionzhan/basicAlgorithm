'''
sort algorithm, such as quicksort  bubble sort
by zhan 2018/11/29
'''


import random

def quickSort(listA,start,end):
    '''
    quicksort algorithm.
    :param listA:待排序数组
    :param start:起始索引
    :param end: 终止索引
    :return: 排好序的列表
    '''
    if start < end:
        baseV = listA[start]
        i,j = start,end
        while i<j:
            while i<j and listA[j] >= baseV:
                j = j-1
            listA[i] = listA[j]

            while i < j and listA[i] <= baseV:
                i = i+ 1
            listA[j] = listA[i]

        listA[i] = baseV

        quickSort(listA,start,i-1)
        quickSort(listA, i+1, end)
    return listA

def bubbleSort(listA):
    '''
    bubble sort algorithm.
    :param listA:
    :return:
    '''
    for i in range(len(listA)):
        for j in range(len(listA)-i-1):
            if listA[j] > listA[j+1]:
                listA[j],listA[j+1] = listA[j+1],listA[j]

    return listA

if __name__ == '__main__':
    listA = [43,61,8,3,1,43,21,32,49,23,9,33,2,5,82,14,17,1]
    listA = [random.randint(0,500) for i in range(17)]
    print(listA)
    # region quick sort
    # print('start quick sort...')
    # print(quickSort(listA,0,len(listA)-1))
    # print('quick sort finish!')
    # endregion

    print('start bubble sort...')
    print(bubbleSort(listA))
    print('bubble sort finish')