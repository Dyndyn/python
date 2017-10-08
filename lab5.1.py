#!/usr/bin/python
#-*- coding: utf-8 -*-


num = input("What's your number? ")

if num & (num-1):
   print('Number %d is NOT power of 2' % num)
else:
   print('Number %d is power of 2' % num)
