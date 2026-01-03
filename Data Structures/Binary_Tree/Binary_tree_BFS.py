from collections import deque

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

# Level Order Traversal (BFS) Time: O(n), Space O(n)
def level_order(node: TreeNode):
  q = deque()
  q.append(node)

  while q:
    node = q.popleft()
    print(node, end=' ')

    if node.left: q.append(node.left)
    if node.right: q.append(node.right)

level_order(a)
