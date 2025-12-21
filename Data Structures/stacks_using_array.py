class Stack:
  def __init__(self, size):
    self.size = size
    self.__stack = [None]*self.size
    self.top = -1

  def push(self, value):
    if self.top == self.size -1:
      return 'overflow'

    self.top += 1
    self.__stack[self.top] = value

  def pop(self):
    if self.top == -1:
      return 'Empty Stack'
    data = self.__stack[self.top]
    self.top -= 1
    return data

  def traverse(self):
    for i in range(self.top + 1):
      print(self.__stack[i], end=' ')
