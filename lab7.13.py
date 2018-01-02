#!/usr/bin/python
#-*- coding: utf-8 -*-
import re

first = input("enter the first string ")
second = input("enter the second string ")

symbols = set(first)

print(set(second).issubset(symbols))

