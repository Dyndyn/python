#!/usr/bin/python
#-*- coding: utf-8 -*-

import math

a = input("What's first number? ")
b = input("What's second number? ")

print('result = %5.3f' % (math.sqrt(a*b) / (math.exp(a)*b) + a*math.exp(2.0*a/b)))
