#!/usr/bin/python
#-*- coding: utf-8 -*-


def quicksort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array

print(quicksort([12,4,5,6,7,3,1,15,7,18,20,2,16]))
print(quicksort(["acx", "asx", "sd", "l"]))
