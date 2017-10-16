#!/usr/bin/python
#-*- coding: utf-8 -*-

import math
from decimal import * 
year = Decimal('1')

summa = Decimal(input("What's the available summa? "))
required = Decimal(input("What's the available summa? "))
percentage = Decimal(input("What's the percentage (within a hundred)? ")/100.0)

def duration(summa, required, percentage):
    return math.ceil(math.log(required/summa, percentage + 1))

print ("duration is %d years" % duration(summa, required, percentage))


