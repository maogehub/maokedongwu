import Queue
q=Queue.LifoQueue()
q.put('message 1')
q.put('message 2')
q.put('message 3')
q.put('message 4')
q.put('message 5')
while not q.empty():
    print q.get()
