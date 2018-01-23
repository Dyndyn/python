#!/usr/bin/python
#-*- coding: utf-8 -*-

from lxml import html
import requests
import csv


class User:
    def __init__(self, number, name, rank, enlightenment, solved) -> None:
        self.number = number
        self.name = name
        self.rank = rank
        self.enlightenment = enlightenment
        self.solved = solved

    def __str__(self) -> str:
        return "{} {} {} {} {}".format(self.number, self.name, self.rank, self.enlightenment, self.solved)


page = requests.get('http://www.codeabbey.com/index/user_ranking')
tree = html.fromstring(page.content)

user_data = tree.xpath('//tr[@class="centered none"]')
# user_data = tree.xpath('//table[@class="table table-striped table-bordered full-width ranking-table"]/node()')

users = []
for index, line in enumerate(user_data):
    try:
        users.append(User(str(line[0].text_content()), str(line[2].text_content()).strip(), str(line[4].text_content()), str(line[5].text_content()), str(line[7].text_content())))
    except Exception as e:
        print(e)

f = open('out.txt', 'wt', encoding='utf8')
# for user in users:
writer = csv.writer(f)
writer.writerow(users)