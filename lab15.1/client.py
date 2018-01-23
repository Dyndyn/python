#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket, select, sys


def prompt():
    sys.stdout.write('<You> ')
    sys.stdout.flush()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999
print("Enter 'exit' to exit")
s.connect((host, port))

while True:
    server_responce = s.recv(1024)
    if server_responce.decode('utf-8').__eq__('Authorized'):
        break
    print(server_responce.decode('utf-8'))
    a = input()
    if a == 'exit':
        break
    s.send(a.encode('utf-8'))

print(s.recv(4096).decode('utf-8'))
prompt()
while True:
    socket_list = [sys.stdin, s]

    # Get the list sockets which are readable
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

    for sock in read_sockets:
        # incoming message from remote server
        if sock == s:
            data = sock.recv(1024)
            if not data:
                print('\nDisconnected from chat server ' + data.decode('utf-8'))
                sock.close()
                sys.exit()
            else:
                # print data
                sys.stdout.write(data.decode('utf-8'))
                prompt()

        # user entered a message
        else:
            msg = sys.stdin.readline()
            s.send(msg.encode('utf-8'))
            prompt()

s.close()