#!/usr/bin/python
#-*- coding: utf-8 -*-

import math

arr = list(input("What's first, second, third side (write using comma)? "))

def square(args):
    args.sort()

    if args[0] + args[1] > args[2]:
        p = sum(args)/2
        return math.sqrt(p*(p-args[0])*(p-args[1])*(p-args[2]))
    else:
        print ("triangle can NOT exist")
print("Square = %f" % square(arr))

