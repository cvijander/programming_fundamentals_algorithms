# try out the Python queue functions
from collections import deque

#todo create a new empty object that will function as queue

queue = deque()

#todo add some items to the queue

queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)

#todo print the queue contents 
print(queue)

#todo pop an item off the front of the queue 
x= queue.popleft()
print(x)
print(queue)