#!/usr/bin/python
#-*- coding: utf-8 -*-

def read_in_chunks(file_object):
    while True:
        data = file_object.readline();
        if not data:
            break
        yield data


class Phone:
    def __init__(self, firstname='', lastname='', number=0):
        self.firstname = firstname
        self.lastname = lastname
        self.number = number

    def __str__(self) -> str:
        return "{} {} - {}".format (self.firstname, self.lastname, self.number)

    def __gt__(self, another):
        if self.lastname != another.lastname:
            return self.lastname.__gt__(another.lastname)
        else:
            return self.firstname.__gt__(another.firstname)

    def init_from_console(self):
        self.firstname = input('Enter first name: ')
        self.lastname = input('Enter last name: ')
        self.number = input('Enter phone: ')

    def __eq__(self, o: object) -> bool:
        return self.number == o.number

    def update(self, property):
        try:
            setattr(self, property, input("Enter " + property + ": "))
        except:
            print('Invalid property')


class PhoneBook:
    def __init__(self):
        self.records = []
        try:
            f = open('data.txt')
            for line in read_in_chunks(f):
                args = line.split()
                self.records.append(Phone(args[0], args[1], args[2]))
            f.close()
        except Exception as e:
            print("Something went wrong!\n" + str(e))

    def finalize(self):
        f = open('data.txt', 'wt', encoding='utf-8')
        for item in self.records:
            f.write('{} {} {}\n'.format(item.firstname, item.lastname, item.number))
        f.flush()
        f.close()

    def add(self):
        record = Phone()
        record.init_from_console()
        self.records.append(record)

    def remove_by_id(self, id):
        self.records.pop(int(id))

    def remove_by_number(self, number):
        for idx, item in enumerate(self.records):
            if str(item.number).__eq__(number):
                self.remove_by_id(idx)


    def search_by_number(self, number):
        for item in self.records:
            if item.number == number:
                return item

    def search_by_name(self, name):
        result = ''
        for item in self.records:
            if (item.firstname + " " + item.lastname).__contains__(name):
                result += '{}\n'.format(item)

        return result

    def update(self, id):
        property = input('Enter property name (firstname, lastname, number): ')
        self.records[int(id)].update(property)

    def sort(self):
        self.records.sort()
        print(self)

    def __str__(self) -> str:
        result = ''
        for idx, val in enumerate(self.records):
            result += '{} - {}\n'.format(idx, val)
        return result


phone_book = PhoneBook()
while True:
    print("1 - add\n2 - remove by id\n3 - remove by number\n4 - show list\n5 - update\n6 - search by number\n"
          "7 - search by name\n8 - sort by name\n9 - exit")
    step = input("Enter id of action: ")
    try:
        if step == '1':
            phone_book.add()
        elif step == '2':
            phone_book.remove_by_id(input('Enter id: '))
        elif step == '3':
            phone_book.remove_by_number(input('Enter number: '))
        elif step == '4':
            print(phone_book)
        elif step == '5':
            phone_book.update(input('Enter id: '))
        elif step == '6':
            print(phone_book.search_by_number(input('Enter number: ')))
        elif step == '7':
            print(phone_book.search_by_name(input('Enter name: ')))
        elif step == '8':
            phone_book.sort()
        elif step == '9':
            phone_book.finalize()
            break
    except Exception as e:
        print("Something went wrong!\n" + str(e))
