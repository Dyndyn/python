#!/usr/bin/python
#-*- coding: utf-8 -*-

weight = input("What's your weight? ")
height = input("What's your height in meters? ")

print('Body weight index %5.2f' %(weight/height**2))
