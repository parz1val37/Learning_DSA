# Heap - A type of Binary Tree
# Heaps or Priority queues

# Binary Tree --> Heapify(to min or max) --> Min/Max Heap

# Min-Heapify: Time O(n), Space O(1)

# Heap Pop (Extract min) : Time O(log n)

class MinHeap:
  def __init__(self):
    self.heap = []

  def __len__(self):
    return len(self.heap)

  def __repr__(self):
    return str(self.heap)

  def insert(self, key, value): # Time O(log n)
    self.heap.append([key, value]) # Append and shift-up to it's correct position
    self._shift_up(len(self.heap)-1)

  def peek(self): # Time: O(1)
    if not self.heap:
      raise IndexError('Empty Heap')
    
    return self.heap[0]

  def pop_min(self): # Time: O(log n)
    if not self.heap:
      raise IndexError('Empty Heap')
    
    min_element = self.heap[0]
    last_element = self.heap.pop()

    if self.heap:
      self.heap[0] = last_element
      self._shift_down(0)

    return min_element

  def _heapify(self, elements): # Time: O(n)
    self.heap = list(elements)

    for i in reversed(range(self._parent(len(self.heap)-1)+1)): # type: ignore
      self._shift_down(i)

  def meld(self, other_heap):
    combined_heap = self.heap + other_heap.heap

    self._heapify(combined_heap)

  def _parent(self, index: int):
    return (index - 1)//2 if index != 0 else None
  
  def _left(self, index):
    left = 2*index + 1
    return left if left < len(self.heap) else None
  
  def _right(self, index):
    right = 2*index + 1
    return right if right < len(self.heap) else None

  def _shift_up(self, index): # swim operation
    parent_index = self._parent(index)

    while parent_index is not None and self.heap[index][0] < self.heap[parent_index][0]:
      self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]

      index = parent_index
      parent_index = self._parent(index)


  def _shift_down(self, index): # sink operaton
    while True:
      smallest = index

      left = self._left(index)
      right = self._right(index)

      if left is not None and self.heap[left][0] < self.heap[smallest][0]:
        smallest = left
      
      if right is not None and self.heap[right][0] < self.heap[smallest][0]:
        smallest = right

      if smallest == index:
        break

      self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]

      index = smallest
