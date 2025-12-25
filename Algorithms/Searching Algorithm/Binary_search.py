def binary_search(arr, target):
  left = 0
  right = len(arr)-1

  while left<=right:
    mid = (right+left)//2
    if arr[mid]==target:
      return mid
    elif arr[mid]<target:
      left = mid + 1
    else:
      right = mid -1
  return False

if __name__=='__main__':
  arr = [-3, 0, 1, 5, 7, 13]
  print(binary_search(arr, 1))
