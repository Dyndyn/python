#!/usr/bin/python
#-*- coding: utf-8 -*-

import decimal

decimal.getcontext().prec = 2
salary = decimal.Decimal(input("What's your salary? "))

tax = salary * decimal.Decimal('0.18')
military = salary * decimal.Decimal('0.015')

print('Податок на доходи фізичних осіб = %.2f, військовий збір = %.2f' % (tax, military))
