#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   rotateArray.py
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Zhan
@Desc    :     寻找旋转数据的最小值
                把一个数组的最开始若干个元素搬到数组末尾，称为旋转数组
                输入递增排序的数组的一个旋转，输出旋转数组的最小元素
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/8/3 22:22   zhan      1.0         None
'''


def minofRotateArray(L, start=0, end=None):
    '''
    寻找旋转数组L的最小值
    :param L: 递增数组的一个旋转
    :param start: 起始索引，默认为0
    :param end: 终止索引，默认为L的最后元素索引
    :return:
    '''

    if end is None:
        end = len(L) - 1

    if len(L) <= 0 \
            or start < 0 or start >= len(L)\
            or end >= len(L) or end < 0 \
            or end < start:
        return None

    if end == start:
        return L[start]

    if end == (start + 1):
        return min(L[start], L[end])

    mid = (start + end) // 2

    if L[mid] > L[start]:
        return minofRotateArray(L, mid, end)

    if L[mid] < L[end]:
        return minofRotateArray(L, start, mid)

    '''1, 0, 1, 1, 1, 1 '''  '''1, 1, 1, 1, 0, 1 '''
    if L[mid] == L[start] and L[mid] == L[end]:
        minV = L[start]
        for i in range(start, end + 1):
            minV = min(L[i], minV)
        return minV
    else:
        print("invalidate input!")
        return None


if __name__ == '__main__':
    L = [1, 0, 1, 1, 1, 1]
    # L = list(range(4, 10)) + list(range(4))
    L = [1, 1, 1, 1, 1, 1, 1, 2, 4, 5, 0, 1, 1, ]
    L = [1, 2, 4, 5, 0, 1, 1, 1, 1, 1, 1, 1, 1, ]
    print(L)
    print(minofRotateArray(L))
