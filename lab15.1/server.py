#!/usr/bin/python3
#-*- coding: utf-8 -*-
import socket
import _thread
import select
import time


def read_in_chunks(file_object):
    while True:
        data = file_object.readline();
        if not data:
            break
        yield data


def on_new_client(clientsocket, addr):
    while True:
        print('Got a connection from {}'.format(addr))
        clientsocket.send('Enter l for login, r for register'.encode('utf-8'))
        client_answer = clientsocket.recv(1024)
        response = client_answer.decode('utf-8')
        if 'l' == response.lower():
                clientsocket.send('Enter login'.encode('utf-8'))
                client_answer = clientsocket.recv(1024)
                login = client_answer.decode('utf-8')
                clientsocket.send('Enter password'.encode('utf-8'))
                client_answer = clientsocket.recv(1024)
                password = client_answer.decode('utf-8')
                if login in credentials and credentials[login] == password:
                    break
                clientsocket.send('Try again'.encode('utf-8'))
        elif 'r' == response.lower():
                clientsocket.send('Enter login'.encode('utf-8'))
                client_answer = clientsocket.recv(1024)
                login = client_answer.decode('utf-8')
                if login in credentials:
                    clientsocket.send('Login already exists'.encode('utf-8'))
                    continue
                clientsocket.send('Enter password'.encode('utf-8'))
                client_answer = clientsocket.recv(1024)
                password = client_answer.decode('utf-8')
                credentials[login] = password
                break
        else:
            continue
    clientsocket.send("Authorized".encode('utf-8'))
    time.sleep(0.5)
    clientsocket.send(("".join(messages)).encode('utf-8'))

    CONNECTION_LIST.append(clientsocket)
    broadcast_data(clientsocket, "[%s:%s] entered room\n" % addr, False)
    print("Client (%s, %s) connected" % addr)


# Function to broadcast chat messages to all connected clients
def broadcast_data(sock, message, add_to_messages=True):
    # Do not send the message to master socket and the client who has send us the message
    for socket in CONNECTION_LIST:
        if socket != serversocket and socket != sock:
            try:
                socket.send(message.encode('utf-8'))
                if add_to_messages:
                    messages.append(message)
            except Exception as e:
                print(e)
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                CONNECTION_LIST.remove(socket)


credentials = {}
f = open('credentials.txt')
for line in read_in_chunks(f):
    arr = line.split()
    credentials[arr[0]] = arr[1]

messages = []
f = open('messages.txt')
for line in read_in_chunks(f):
    messages.append(line)

CONNECTION_LIST = []
RECV_BUFFER = 1024

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9999
serversocket.bind((host, port))
serversocket.listen(10)
print('the server is waiting for connection')
CONNECTION_LIST.append(serversocket)
try:
    while True:
        # Get the list sockets which are ready to be read through select
        read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

        for sock in read_sockets:
            # New connection
            if sock == serversocket:
                # Handle the case in which there is a new connection recieved through server_socket
                sockfd, addr = serversocket.accept()
                _thread.start_new_thread(on_new_client, (sockfd, addr))


            # Some incoming message from a client
            else:
                # Data recieved from client, process it
                try:
                    # In Windows, sometimes when a TCP program closes abruptly,
                    # a "Connection reset by peer" exception will be thrown
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data.decode('utf-8'))

                except Exception as e:
                    print(e)
                    broadcast_data(sock, "Client (%s, %s) is offline" % addr)
                    print("Client (%s, %s) is offline" % addr)
                    sock.close()
                    CONNECTION_LIST.remove(sock)
                    continue

except KeyboardInterrupt:
    f = open('credentials.txt', 'wt', encoding='utf-8')
    for key, value in credentials.items():
        f.write(key + ' ' + value + '\n')

    f = open('messages.txt', 'wt', encoding='utf-8')
    for value in messages:
        f.write(value)

