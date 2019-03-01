import socket
import threading
import pygame
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#sock.bind(("0.0.0.0", 5555))

server = ''

port = 5555

#sock.listen(2)

connections = []

try:
    sock.bind((server, port))

except socket.error as x:
    print(str(x))

print("Connecting...")

def handler(c, a):
    global connections
    while True:
        data = c.recv(1024)
        for connection in connections:
            connection.send(bytes(data))
        if not data:
            connections.remove(c)
            c.close()
            break
        conn.sendall(data)

while True:
    c, a = sock.accept()
    cThread = threading.Thread(target=handler, args=(c,a))
    cThread.daemon = True
    cThread.start()
    connections.append(c)
    print(connections)
