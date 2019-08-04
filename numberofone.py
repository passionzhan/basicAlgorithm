#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   numberofone.py    
@Contact :   9824373@qq.com
@License :   (C)Copyright 2017-2018, Zhan
@Desc    :     判断给定的正整数二进制表示中1 的个数
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/8/4 15:22   zhan      1.0         None
'''
import sys

def numberofone(n):
    '''

    :param n:
    :return:
    '''

    rstCount = 0

    while n:
        rstCount += 1
        n = (n-1) & n
    return rstCount

def numberofone2(n):
    rstCount = 0
    flag = 1
    loopNum = sys.getsizeof(n) * 8

    while loopNum > 0:
        if flag & n:
            rstCount += 1
        flag = flag << 1
        loopNum -= 1

    return rstCount

if __name__ == '__main__':
    # a = 10
    # print(sys.getsizeof(9))
    # print(sys.getsizeof(9))


    # print(numberofone(9))
    # print(numberofone2(9))
    # print(numberofone(3))
    # print(numberofone2(3))
    # print(numberofone(15))
    # print(numberofone2(15))
    # print(numberofone(0))
    # print(numberofone2(0))
    # print(numberofone(-9))



