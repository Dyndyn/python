#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys

if len(sys.argv) < 3:
    print('Arguments are incorrect')
else:
    print('Вітаю, {} {}'.format(sys.argv[1], sys.argv[2]))
