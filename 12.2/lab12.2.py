#!/usr/bin/python
#-*- coding: utf-8 -*-
import math


class Star:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "%s %.2f %.2f" % (self.name ,self.x, self.y)

    def _length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def rotate(self, rotate_degree):
        start_degree = math.atan(self.y/self.x)
        if self.x > 0 and self.y < 0:
            start_degree = start_degree + math.pi*2
        elif self.x < 0:
            start_degree = start_degree + math.pi
        elif self.x == 0 and self.y > 0:
            start_degree = math.pi / 2
        elif self.x == 0 and self.y < 0:
            start_degree = math.pi * 3 / 2

        degree = start_degree + (rotate_degree / 180 * math.pi)
        length = self._length()
        self.x = round(math.cos(degree) * length, 4)
        self.y = round(math.sin(degree) * length, 4)

    def __gt__(self, star):
        if self.y != star.y:
            return self.y > star.y
        else:
            return self.x > star.x


f = open('12.2/in.txt', 'r+t', encoding='utf-8')

first_line = f.readline().split()
number = int(first_line[0])
degree = int(first_line[1])
stars = []

for line in f:
    args = line.split()
    stars.append(Star(args[0], float(args[1]), float(args[2])))

f.close()

for star in stars:
    star.rotate(degree)

stars.sort()

f = open('12.2/out.txt', 'wt', encoding='utf-8')
f.write(' '.join(map(str, (star.name for star in stars))))
f.flush()
f.close()
