# EPOLL

python 官方文档的 select 模组中，有介绍到 epoll 

但是似乎没有给任何 epoll 的例子

这里给两个epoll的例子，一个是tcp的，一个是udp的

程序源码可以在：[这里](../src/epoll) 看到

[tcp_poll.py](../src/epoll/tcp_epoll.py)

~~~python
#!/usr/bin/python
import socket
import select
import sys

debug=False
socket.setdefaulttimeout(5)
EOL1='\n\n'
EOL2='\n\r\n'
response = 'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\nServer: Python2.7_Raw_Socket\r\n'
response += 'Content-Type: text/plain\r\nContent-Length: 1024\r\n\r\n'
response += 'H'*1024

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversocket.bind(('0.0.0.0', 8080))
serversocket.listen(100)
serversocket.setblocking(0)

epoll=select.epoll()
epoll.register(serversocket.fileno(), select.EPOLLIN)

try:
    connections = {}; requests = {}; responses={}
    while True:
        events = epoll.poll(1)
        for fileno, event in events:
            if fileno == serversocket.fileno():
                connection, address = serversocket.accept()
                connection.setblocking(0)
                epoll.register(connection.fileno(), select.EPOLLIN)
                connections[connection.fileno()] = connection
                requests[connection.fileno()]=''
                responses[connection.fileno()]=response
                if debug:
                    print ("+%s" %connection.fileno(), "setup new connection, register to epoll", address, "connections ", len(connections), connections.keys())
            elif event & select.EPOLLIN:
                data = connections[fileno].recv(1024)
                if not data:
                    epoll.unregister(fileno)
                    connections[fileno].close()
                    del connections[fileno]
                    continue
                requests[fileno] += data
                if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                    epoll.modify(fileno, select.EPOLLOUT)
            elif event & select.EPOLLOUT:
                byteswritten = connections[fileno].send(responses[fileno])
                responses[fileno] = responses[fileno][byteswritten:]
                if len(responses[fileno])==0:
                    epoll.modify(fileno, 0)
                    connections[fileno].shutdown(socket.SHUT_RDWR)
            elif event & select.EPOLLHUP:
                if debug:
                    print "-%s" %fileno
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]
                if debug:
                    print ("ok:%s" %fileno, "unregister EPOLLHUP", "in delete: connections", len(connections), connections.keys())
finally:
    print ("in finally: connections, request, response", len(connections), len(requests), len(responses))
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()
~~~

[udp_epoll.py](../src/epoll/udp_epoll.py) UDP 只有做EPOLLIN，没有做OUT了，跟TCP是一样的原理的

~~~python
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
~~~
