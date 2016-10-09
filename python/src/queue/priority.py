import Queue
q=Queue.PriorityQueue()
q.put((5, 'priority 5'))
q.put((3, 'priority 3'))
q.put((1, 'priority 1'))
q.put((2, 'priority 2'))
q.put((4, 'priority 4'))
while not q.empty():
    print q.get()
