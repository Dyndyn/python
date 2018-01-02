#!/usr/bin/python
#-*- coding: utf-8 -*-
from collections import deque

n = input("enter N? ")
k = input("enter K? ")
cycle = deque(range(1, int(n)+1))

while cycle.__len__() > 1:
    cycle.rotate(-int(k))
    print(cycle.pop())

print ("last {}".format(cycle[0]))


