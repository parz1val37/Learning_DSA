def binary_search(list: list[int], target: int):
  # List should be sorted in ascending order
  first = 0
  last = len(list) -1
  while first<=last:
    mid = (first + last)//2
    if list[mid]==target:
      return mid
    elif list[mid]<target:
      first = mid + 1
    else:
      last = mid - 1
  return None

def verify(index):
  if index is not None:
    print(f"Target found at index: {index}")
  else:
    print("Target not found in the list")

nums = [0, 1, 5 , 9, 13, 17, 21, 27, 28, 33, 37, 44]
result = binary_search(nums, 33)
verify(result)
