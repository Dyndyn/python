#!/usr/bin/python
#-*- coding: utf-8 -*-


def next_rand(seed=654321):
    while True:
        x = str(seed)
        if len(x)!=6:
            x = (6 - len(x)) * '0' + x
        y = x[3:6] + x[0:3]
        product = str(int(x) * int(y))
        if len(product)!=12:
            product = (12 - len(product)) * '0' + product
        seed = product[3:9]
        yield int(seed)

a=next_rand()
for i in range(10):
    print(a.__next__())