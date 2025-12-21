class Node:
  def __init__(self, data) -> None:
    self.data = data
    self.next = None

class Stack:
  def __init__(self) -> None:
    self.top = None # type: ignore

  def __len__(self):
    temp = self.top
    len = 0
    while temp != None:
      len += 1
      temp = temp.next
    return len

  def is_empty(self) -> bool:
    return self.top == None

  def push(self, value) -> None:
    new_node: Node = Node(value)
    new_node.next = self.top # type: ignore
    self.top = new_node

  def traverse(self) -> None:
    temp = self.top
    while temp != None:
      print(temp.data)
      temp = temp.next

  def peek(self):
    if self.is_empty():
      return "Empty stack"
    return self.top.data # type: ignore

  def pop(self):
    if self.is_empty():
      return 'Empty stack'
    top_data = self.top.data # type: ignore
    self.top = self.top.next # type: ignore
    return top_data
