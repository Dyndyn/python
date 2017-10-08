#!/usr/bin/python
#-*- coding: utf-8 -*-

import random

print ("1 - камінь, 2 - ножиці, 3 - папір, 0 - завершити")
arr=["камінь","ножиці", "папір"]
while True:
    choice = input("Ваш вибір? ")
    if choice==0: break

    rand = random.randint(1, 3)
    print("Комп'ютер - " + arr[rand-1] + ", Ви - " + arr[choice - 1])

    if (choice, rand) in ((1,2), (2,3), (3,1)):
        print('Ви перемогли')
    elif choice == rand:
        print('Нічия')
    else:
        print('Ви програли')
