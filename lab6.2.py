#!/usr/bin/python
#-*- coding: utf-8 -*-

from decimal import * 
cents = Decimal('0.01')

summa = input("What's the summa? ")
percentage = Decimal(input("What's the percentage (within a hundred)? ")/100.0)
duration = input("What's the duration (in years)? ")

def funct(summa, percentage, duration):
    result = Decimal(summa)
    i = 0
    while i < duration:
        result = (result + result*percentage).quantize(cents, ROUND_HALF_UP)
        i = i + 1
    return result

print ("result = %.2f" % funct(summa, percentage, duration))


