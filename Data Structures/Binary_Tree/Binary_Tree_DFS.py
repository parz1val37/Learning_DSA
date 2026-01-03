class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.value = val
    self.left = left
    self.right = right

  def __str__(self):
    return str(self.value)

# creating this tree
'''      7
    6         8
  3   10    4   9
'''
# creating nodes for tree
a = TreeNode(7)
b = TreeNode(6)
c = TreeNode(3)
d = TreeNode(10)
e = TreeNode(8)
f = TreeNode(4)
g = TreeNode(9)

a.left = b
a.right = e
b.left = c
b.right = d
e.left = f
e.right = g

# Recursive pre-order(node-left-right) traversal (DFS), Time: O(n) | Space: O(n)
def pre_order_dfs(node):
  if not node:
    return
  
  print(node, end=' ')
  pre_order_dfs(node.left)
  pre_order_dfs(node.right)

# pre_order_dfs(b)
# print()

# Recursive In-Order(Left-Node-Right) traversal (DFS), Time: O(n) | Space: O(n)
def in_order_dfs(node):
  if not node:
    return
  
  in_order_dfs(node.left)
  print(node, end=' ')
  in_order_dfs(node.right)

# in_order_dfs(b)
# print()

# Recursive Post-Order(Left-Right-Node) traversal (DFS), Time: O(n) | Space: O(n)
def post_order_dfs(node):
  if not node:
    return
  
  post_order_dfs(node.left)
  post_order_dfs(node.right)
  print(node, end=' ')

post_order_dfs(b)
