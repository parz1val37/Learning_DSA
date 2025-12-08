class Node:
  def __init__(self, value):
    self.data = value
    self.next = None

class LinkedList:
  def __init__(self):
    # Empty Linked list -- 0 nodes
    self.head = None
    self.n = 0

  def __str__(self):
    if self.head == None:
      return 'Empty LinkedList'
    curr  = self.head
    result = ''
    while curr != None:
      result += str(curr.data) + '->'
      curr  = curr.next
    return result[:-2]

  def __len__(self):
    # No. of nodes
    return self.n

  def __getitem__(self, index):
    if 0 <= index < self.n:
      curr = self.head
      pos = 0
      while curr != None:
        if pos == index:
          return curr.data
        curr = curr.next
        pos += 1
      print("item not found!")
    raise IndexError("Out of index")

  def clear(self):
    self.head = None
    self.n = 0

  def insert_head(self, value):
    # New Node
    new_node = Node(value)
    # Create connection
    new_node.next = self.head
    # Reassign head
    self.head = new_node
    self.n += 1

  def delete_head(self):
    if self.head == None:
      raise ValueError("Empty LinkedList")
    self.head = self.head.next
    self.n -= 1

  def append(self, value):
    new_node = Node(value)
    # if list is empty
    if self.head == None:
      self.head = new_node
      self.n += 1
      return

    curr = self.head
    while curr.next != None:
      curr = curr.next
    # You're at the last Node
    curr.next = new_node
    self.n += 1

  def insert_after(self, after, value):
    new_node = Node(value)

    if self.head != None:
      curr = self.head
      while curr.data != after:
        curr = curr.next
        if curr == None:
          raise ValueError("Value not in the list")
      new_node.next = curr.next
      curr.next = new_node
      self.n += 1
    else:
      raise ValueError("Empty list")

  def pop(self):
    if self.head == None:
      raise ValueError("Empty LinkedList")
    curr = self.head
    if curr.next == None:
      self.delete_head()
    else:
      while curr.next.next != None:
        curr = curr.next
      # Now curr -> 2nd last Node
      curr.next = None
      self.n -= 1

  def remove(self, value):
    if self.head == None:
      raise ValueError("Empty LinkedList")

    if self.head.data == value:
      self.delete_head()
      return

    curr = self.head
    while curr.next != None:
      if curr.next.data == value:
        break
      curr = curr.next
    #case: Item not in the list
    if curr.next == None:
      return "Item not found"
    else:
      curr.next = curr.next.next
      self.n -= 1

  def find(self, value):
    if self.head == None:
      raise ValueError("Empty LinkedList")

    curr = self.head
    index = 0
    while curr != None:
      if curr.data == value:
        return index
      curr = curr.next
      index += 1
    print(f"{value}, Not found in the list")
