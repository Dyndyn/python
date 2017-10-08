#!/usr/bin/python
#-*- coding: utf-8 -*-


arr = list(input("What's first, second, third side (write using comma)? "))
arr.sort()

if arr[0] + arr[1] > arr[2]:
    print ("triangle can exist")
else:
    print ("triangle can NOT exist")
