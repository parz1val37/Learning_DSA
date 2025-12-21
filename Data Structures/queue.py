# FIFO -- First In First out
# [head/front] -> [] -> [] -> [] -> [] -> [tail / rear]
# insertion - enqueue, insert from tail
# deletion - dequeue, delete from head

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self) -> None:
    self.front = None
    self.rear = None

  # inserting data in queue
  def enqueue(self, value):
    new_node = Node(value)

    if self.rear == None:
      self.front = new_node
      self.rear = self.front
    else:
      self.rear.next = new_node # type: ignore
      self.rear = new_node
  
  # deleting head from queue
  def dequeue(self):
    if self.front == None:
      print('Empty queue')
    else:
      self.front = self.front.next

  # traversing to see data in queue
  def traverse(self):
    if self.rear == None:
      print('Empty queue')
      return
    
    temp = self.front
    while temp != None:
      print(temp.data, end=' ')
      temp = temp.next

  # function to check if queue is empty or not
  def is_empty(self) -> bool:
    return self.rear == None
  
  # function to get size of queue
  def size(self) -> int:
    if self.is_empty():
      return 0
    temp = self.front
    size = 0
    while temp != None:
      size += 1
      temp = temp.next
    return size

  # func to get front item of queue
  def front_item(self):
    if self.is_empty():
      return 'Empty queue'
    
    return self.front.data # type: ignore

  # func to get rear item of queue
  def rear_item(self):
    if self.is_empty():
      return 'Empty queue'
    
    return self.rear.data # type: ignore