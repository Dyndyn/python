#!/usr/bin/python
#-*- coding: utf-8 -*-
import datetime


class Record:
    def __init__(self, task='', deadline=datetime.datetime.now(), priority='normal', comment='', status='in process'):
        self.task = task
        self.deadline = deadline
        self.priority = priority
        self.comment = comment
        self.status = status

    def __str__(self) -> str:
        return "{} {} {}; {}; {}".format (self.task ,self.deadline, self.priority, self.status, self.comment)

    def __gt__(self, another):
        self.deadline.__gt__(another.deadline)

    def init_from_console(self):
        self.task = input('Enter Task: ')
        dt = input('Enter date (dd/mm/yyyy): ')
        try:
            self.deadline = datetime.datetime.strptime(dt, '%d/%m/%Y')
        except:
            self.deadline = datetime.datetime()
        self.priority = input('Enter Priority: ')
        self.comment = input('Enter Comment: ')
        self.status = input('Enter Status: ')

    def __eq__(self, o: object) -> bool:
        if o is not Record or self.task != o.task or self.deadline != o.deadline or self.priority != o.priority\
            or self.status != o.status:
                return False
        else:
            return True

    def update(self, property):
        try:
            if property != 'deadline':
                setattr(self, property, input("Enter " + property + ": "))
            else:
                setattr(self, property, datetime.datetime.strptime(input("Enter " + property + "(dd/mm/yyyy): "), '%d/%m/%Y'))
        except:
            print('Invalid property')


class ToDoList:
    def __init__(self):
        self.records = []

    def add(self):
        record = Record()
        record.init_from_console()
        self.records.append(record)

    def remove(self, obj):
        if obj is int or str(obj).isdigit():
            self.records.pop(int(obj))
        else:
            for item in self.records:
                if item.task == obj:
                    self.records.remove(item)

    def search_by_task(self, task):
        for item in self.records:
            if item.task == task:
                return item

    def mark_solved(self, id):
        self.records[int(id)].status = 'Solved'

    def update(self, id):
        property = input('Enter property name (task, deadline, priority, comment, status): ')
        self.records[int(id)].update(property)

    def __str__(self) -> str:
        result = ''
        for idx, val in enumerate(self.records):
            result += '{} - {}\n'.format(idx, val)
        return result


to_do_list = ToDoList()
to_do_list.records.append(Record('lab14.1', datetime.datetime(2018, 1, 24), 'High', '', 'In Process'))
to_do_list.records.append(Record('lab14.2', datetime.datetime(2018, 1, 24), 'High', '', 'Pending'))
to_do_list.records.append(Record('lab19.1', datetime.datetime(2018, 1, 24), 'Urgent', '', 'Pending'))
while True:
    print("1 - add\n2 - remove by id or task\n3 - show list\n4 - search by task\n5 - mark as solved\n6 - update\n"
          "7 - exit")
    step = input("Enter id of action: ")
    try:
        if step == '1':
            to_do_list.add()
        elif step == '2':
            to_do_list.remove(input('Enter id or task: '))
        elif step == '3':
            print(to_do_list)
        elif step == '4':
            print(to_do_list.search_by_task(input('Enter task: ')))
        elif step == '5':
            to_do_list.mark_solved(input('Enter id: '))
        elif step == '6':
            to_do_list.update(input('Enter id: '))
        elif step == '7':
            break
    except Exception as e:
        print("Something went wrong!\n" + str(e))
