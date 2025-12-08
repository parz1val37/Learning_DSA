def linear_search(list_num, target):
  # returns the index of the target or returns None.
  for i in range(len(list_num)):
    if list_num[i] == target:
      return i
  return None

def verify(index):
  if index is not None:
    print(f"Target found at index: {index}")
  else:
    print(f"Target not found in the list.")

nums = [1, 4, 6, 8, 4, 9, 0]

result = linear_search(nums, 6)
verify(result)
verify(linear_search(nums, 0))
