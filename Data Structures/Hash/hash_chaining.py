# array of  linkedList

class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    # Empty Linked list -- 0 nodes
    self.head = None

  def traverse(self):
    temp = self.head
    while temp != None:
      print(f'{temp.key}: {temp.value}', end=' ')
      temp = temp.next

  def append(self, key, value):
    new_node = Node(key, value)
    # if list is empty
    if self.head == None:
      self.head = new_node
      return

    curr = self.head
    while curr.next != None:
      curr = curr.next
    # You're at the last Node
    curr.next = new_node # type: ignore

  def pop(self):
    if self.head == None:
      raise ValueError("Empty LinkedList")
    curr = self.head
    if curr.next == None:
      self.head = None
      return
    else:
      while curr.next.next != None: # type: ignore
        curr = curr.next # type: ignore
      # Now curr -> 2nd last Node
      curr.next = None # type: ignore

  def remove(self, key):
    if self.head == None:
      raise ValueError("Empty LinkedList")

    if self.head.key == key:
      self.head = self.head.next
      return

    curr = self.head
    while curr.next != None:
      if curr.next.key == key:
        break
      curr = curr.next
    #case: Item not in the list
    if curr.next == None:
      return "Item not found"
    else:
      curr.next = curr.next.next

  def search(self, key):
    curr = self.head
    index = 0
    while curr != None:
      if curr.key == key:
        return index
      curr = curr.next
      index += 1
    return -1

  def get_node_at_index(self, index):
    temp = self.head
    counter = 0
    while temp != None:
      if counter == index:
        return temp
      temp = temp.next
      counter += 1

  def size(self):
    temp = self.head
    count = 0
    while temp != None:
      count += 1
      temp = temp.next
    return count

class Dictionary:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.size = 0
    # create array of LinkedList
    self.buckets = self.make_array(self.capacity)

  def make_array(self, capacity: int):
    l = []
    for i in range(capacity):
      l.append(LinkedList())
    return l

  def hash_value(self, key):
    return abs(hash(key))%self.capacity

  def put(self, key, value):
    bucket_index = self.hash_value(key)

    def get_node_index(bucket_index, key):
      node_index = self.buckets[bucket_index].search(key)
      return node_index

    node_index = get_node_index(bucket_index, key)

    if node_index == -1:
      self.buckets[bucket_index].append(key, value)
      self.size += 1

      load_factor = self.size/self.capacity
      # print(load_factor)
      if load_factor >= 2:
        self.rehash()
    else:
      node = self.buckets[bucket_index].get_node_at_index(node_index)
      node.value = value

  def __setitem__(self, key, value):
    return self.put(key, value)

  def rehash(self):
    self.capacity *= 2
    old_buckets = self.buckets
    self.size = 0
    self.buckets = self.make_array(self.capacity)

    for linkedlist in old_buckets:
      for index in range(linkedlist.size()):
        node = linkedlist.get_node_at_index(index)
        key_item = node.key
        value_item = node.value
        self.put(key_item, value_item)

  def get(self, key):
    bucket_index = self.hash_value(key)
    response = self.buckets[bucket_index].search(key)

    if response == -1:
      return -1
    else:
      node = self.buckets[bucket_index].get_node_at_index(response)
      return node.value

  def __getitem__(self, key):
    value = self.get(key)
    if value == -1:
      raise ValueError('Item not available')
    return value
  
  def __delitem__(self, key):
    bucket_index = self.hash_value(key)
    self.buckets[bucket_index].remove(key)
    self.size -= 1

  def __str__(self):
    for linkedlist in self.buckets:
      linkedlist.traverse()
    return ''
  
  def __len__(self):
    return self.size
