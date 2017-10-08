#!/usr/bin/python
#-*- coding: utf-8 -*-

import math
num = input("What's your number? ")

i = 2
while i <= math.floor(math.sqrt(num)):
    if (num / float(i) % 1 == 0):
        print("{} / {} % 1 = {}".format(num, i, num / i % 1))
        print("%d is not prime" % num)
        exit()
    i+=1
print("%d is prime" % num)
