#!/usr/bin/python
#-*- coding: utf-8 -*-

import math

a = input("What's a coefficient? ")
b = input("What's b coefficient? ")
c = input("What's c coefficient? ")

D = b**2 - 4*a*c

if D < 0: print("quadratic equation doesn't have solutions")
elif D == 0: print("quadratic equation has one solution - %f" % (-b/(2.0*a)))

else:
    sol1 = (-b + math.sqrt(D))/(2.0 * a)
    sol2 = (-b - math.sqrt(D))/(2.0 * a)
     
    print("quadratic equation has two solutions - %f and %f" % (sol1, sol2))
