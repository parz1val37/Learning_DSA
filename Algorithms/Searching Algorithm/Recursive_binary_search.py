def recursive_binary_search(arr, target):
  if len(arr)==0:
    return False
  else:
    mid = len(arr)//2
    if arr[mid]==target:
      return True

    else:
      if arr[mid]<target:
        return recursive_binary_search(arr[mid+1:], target)
      return recursive_binary_search(arr[:mid], target)

if __name__=='__main__':
  arr = [-3, 0, 1, 5, 7, 13]
  print(recursive_binary_search(arr, 1))
