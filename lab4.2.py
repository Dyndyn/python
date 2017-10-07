#!/usr/bin/python
#-*- coding: utf-8 -*-

import math

x = input("What's first number? ")
u = input("What's second number? ")
o = input("What's third number? ")

print('result = %5.3f' % (1/(o*math.sqrt(2*math.pi)) * math.exp(-(x-u)**2/(2*o**2))))
