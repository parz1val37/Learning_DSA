# Dict class using Hashing | Linear probing

class Dictionary:
  def __init__(self, size: int):
    self.size = size
    self.slots = [None]*self.size
    self.data = [None]*self.size

  def hash_func(self, key) -> int:
    return abs(hash(key)) % self.size

  def rehash(self, old_hash) -> int:
    return (old_hash + 1) % self.size

  def put(self, key, value):
    hash_value = self.hash_func(key)
    if self.slots[hash_value] == None:
      self.slots[hash_value] = key
      self.data[hash_value] = value
    else:
      if self.slots[hash_value] == key:
        self.data[hash_value] = value
      else:
        new_hash_value = self.rehash(hash_value)
        while self.slots[new_hash_value] != None and self.slots[new_hash_value] != key:
          new_hash_value = self.rehash(new_hash_value)

        if self.slots[new_hash_value] == None:
          self.slots[new_hash_value] = key
          self.data[new_hash_value] = value
        else:
          self.data[new_hash_value] = value

  def __setitem__(self, key, value):
    self.put(key, value)

  def __getitem__(self, key):
    return self.get(key)

  def get(self, key):
    start_pos = self.hash_func(key)
    current_pos = start_pos

    while self.slots[current_pos] != None:
      if self.slots[current_pos] == key:
        return self.data[current_pos]
      
      current_pos = self.rehash(current_pos)

      if current_pos == start_pos:
        return 'Not Found'
    return 'Not Found'
  
  def __str__(self):
    for i in range(self.size):
      if self.slots[i] != None:
        print(f'{self.slots[i]}: {self.data[i]}', end=" ")
    return ''
