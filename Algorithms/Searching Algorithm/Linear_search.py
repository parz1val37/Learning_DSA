# Brute-Force, Time Complexity: O(n), Space Complexity: O(1)
def Linear_Search(arr, target):
  for item in arr:
    if item==target: return True
  return False
