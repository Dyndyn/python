#!/usr/bin/python
#-*- coding: utf-8 -*-

from decimal import *

#getcontext().prec = 2
cents = Decimal('0.01')
salary = Decimal(input("What's your salary? ")).quantize(cents, ROUND_HALF_UP)

tax = (salary * Decimal('0.18')).quantize(cents, ROUND_HALF_UP)
military = (salary * Decimal('0.015')).quantize(cents, ROUND_HALF_UP)

print('Податок на доходи фізичних осіб = %.2f, військовий збір = %.2f' % (tax, military))
