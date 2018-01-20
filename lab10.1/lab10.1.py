#!/usr/bin/python
#-*- coding: utf-8 -*-
from shutil import copyfile

text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'


def write2begin(text, offset=34, step=2000, src='initial.bmp', dest='result.bmp'):
    copyfile(src, dest)

    f = open(dest, 'r+b')

    f.seek(offset)
    for i in text:
        f.write(bytearray(i, 'UTF-8'))
        f.seek(step,1)

    f.flush()
    f.close()


def read_from_begin(size, offset=34, step=2000, src='result.bmp'):
    f = open(src, 'r+b')

    f.seek(offset)
    result = b''
    for i in range(size):
        result = result + f.read(1)
        f.seek(step,1)
    f.close()
    return result


write2begin(text)
print(read_from_begin(74))