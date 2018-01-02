#!/usr/bin/python
#-*- coding: utf-8 -*-


def mean(array):
    return sum(array) / len(array)


def median(array):
    array = sorted(array)
    if len(array) % 2 == 1:
        return array[len(array)//2]
    else:
        return (array[len(array)//2-1] + array[len(array)//2]) / 2


print(mean([12,4,5,6,7,3,1,15,7,18,20,2,16]))
print(median([12,4,5,6,7,3,1,15,7,18,20,2,16]))