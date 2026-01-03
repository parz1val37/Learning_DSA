class BinaryTree:
  def __init__(self, root_value, left=None, right=None):
    self.value = root_value
    self.left = left
    self.right = right

  def __str__(self) -> str:
    return str(self.value)

  def in_order_dfs(self):
    if self.left:
      self.left.in_order_dfs()

    print(self.value, end=' ')
    
    if self.right:
      self.right.in_order_dfs()

  def insert(self, value: int):
    if value < self.value:
      if self.left is None:
        self.left = BinaryTree(value)
      else:
        self.left.insert(value)
    else:
      if self.right is None:
        self.right = BinaryTree(value)
      else:
        self.right.insert(value)
  
  def search(self, target):
    if target < self.value:
      if self.left is None:
        return False
      return self.left.search(target)
    
    elif self.value == target:
      return True
    
    else:
      if self.right is None:
        return False
      return self.right.search(target)



btr = BinaryTree(6) 
btr.insert(15)
btr.insert(8)
btr.insert(-7)
btr.insert(7)
btr.insert(3)
btr.insert(10)
btr.insert(11)
btr.insert(-1)
# print(btr)
# btr.in_order_dfs()
print(btr.search(3))
