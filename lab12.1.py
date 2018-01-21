#!/usr/bin/python
#-*- coding: utf-8 -*-
import math


class Point:
    def __new__(cls, x=0, y=0):
        inst = object.__new__(Point)
        inst.x = x
        inst.y = y
        return inst

    def __str__(self) -> str:
        return "Point(x = {}, y = {})".format(self.x, self.y)

    def diff_length(self, point) -> float:
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


class Triangle:
    def __new__(cls, a=Point(), b=Point(), c=Point()):
        inst = object.__new__(Triangle)
        inst.a = a
        inst.b = b
        inst.c = c
        return inst

    def __str__(self) -> str:
        return "Triangle(a = {}, b = {}, c = {})".format(self.a, self.b, self.c)

    def is_valid(self) -> bool:
        x = self.a.diff_length(self.b)
        y = self.a.diff_length(self.c)
        z = self.b.diff_length(self.c)
        return x + y > z and x + z > y and y + z > x

    def perimeter(self) -> float:
        x = self.a.diff_length(self.b)
        y = self.a.diff_length(self.c)
        z = self.b.diff_length(self.c)
        return x + y + z

    def square(self) -> float:
        x = self.a.diff_length(self.b)
        y = self.a.diff_length(self.c)
        z = self.b.diff_length(self.c)
        p = (x + y + z) / 2
        return math.sqrt((p - x) * (p - y) * (p - z) * p)


point1 = Point(3,4)
point2 = Point()
print("{} - {} = {}".format(point1, point2, point1.diff_length(point2)))

a = Point()
b = Point(3, 0)
c = Point(0, 4)

triangle = Triangle(a,b,c)
print("is valid = {}".format(triangle.is_valid()))
print("perimeter = {}, square = {}".format(triangle.perimeter(), triangle.square()))
