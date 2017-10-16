#!/usr/bin/python
#-*- coding: utf-8 -*-

import math

arr = list(input("What's first, second, third side (write using comma)? "))
arr.sort()

if arr[0] + arr[1] > arr[2]:
    p = sum(arr)/2
    square = math.sqrt(p*(p-arr[0])*(p-arr[1])*(p-arr[2]))
    print("Square = %f" % square)
else:
    print ("triangle can NOT exist")
