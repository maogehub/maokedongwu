#!/usr/bin/python
import socket
import select

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 1234))
serversocket.setblocking(0)
epoll=select.epoll()
epoll.register(serversocket.fileno(), select.EPOLLIN)
try:
    while True:
        events = epoll.poll(1)
        for lineno, event in events:
            if event & select.EPOLLIN:
                data, (ip, port) = serversocket.recvfrom(1024)
                print ip, port, data
finally:
    print ("in finally")
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()
