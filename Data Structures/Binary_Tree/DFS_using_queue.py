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

# Check if value exists (DFS) Time: O(n), Space O(n)
def search_dfs(node, target):
  if not node:
    return False

  if node.value == target:
    return True

  return search_dfs(node.left, target) or search_dfs(node.right, target)

print(search_dfs(a, 11))
