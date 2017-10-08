#!/usr/bin/python
#-*- coding: utf-8 -*-


door = list(input("What's height and width of door (write using comma)? "))
door.sort()

arr = list(input("What's a, b, c (write using comma)? "))
arr.sort()

if arr[1] <= door[1] and arr[0] <= door[0]:
    print("There is way to fit the box through the door.")
else:
    print("There is NO way to fit the box through the door.")

