#!/usr/bin/python
#-*- coding: utf-8 -*-
import itertools

n = input("What's N? ")
k = input("What's K? ")
cycled = list(range(1, int(n) + 1))
iterable = iter(cycled)

while cycled.__len__():
    elem = 0
    for _ in range(int(k)):
        try:
            elem = iterable.__next__()
        except StopIteration:
            iterable = iter(cycled)
    print(elem)
    cycled.remove(elem)
    if cycled.__len__() == 1:
        break

print ("last {}".format(cycled))


