#!/usr/bin/python
#-*- coding: utf-8 -*-

from lxml import html, cssselect
import requests
import csv


class Notebook:
    def __init__(self, name, price, description, link, img_link) -> None:
        self.name = name
        self.price = price
        self.description = description
        self.link = link
        self.img_link = img_link

    def __str__(self) -> str:
        return "{} {} {} {} {}".format(self.name, self.price, self.description, self.link, self.img_link)


page = requests.get('http://price.ua/catc839t14.html?price[min]=10000&price[max]=20000')
tree = html.fromstring(page.content)

data = tree.xpath('//div[@class="white-wrap clearer-block"]')

notebooks = []
for line in data:

    name =  line.cssselect('a.model-name')[0].text_content()
    try:
        price =  line.cssselect('span.price')[-1].text_content()
    except Exception as e:
        price = line.cssselect('a.price')[-1].text_content()
    description = {}
    for span in line.cssselect('div.item'):
        arr = span.text_content().split('-')
        description[arr[0].strip()] = arr[1].strip()
    link = line.cssselect('a.model-name')[0].get('href')
    img_link = line.cssselect('img')[0].get('src')
    notebooks.append(Notebook(name, price, description, link, img_link))

f = open('out.txt', 'wt', encoding='utf8')

writer = csv.writer(f)
writer.writerow(notebooks)