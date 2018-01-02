#!/usr/bin/python
#-*- coding: utf-8 -*-
import re

s = input("enter the email address ")

print(True if re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,}$", s) else False)

