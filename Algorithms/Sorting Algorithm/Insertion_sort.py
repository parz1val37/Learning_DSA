# Time: O(n²), Space: O(1)

def Insertion_sort(arr):
  for i in range(1, len(arr)):
    j = i
    while j > 0 and arr[j-1] > arr[j]:
      arr[j-1], arr[j] = arr[j], arr[j-1]
      j -= 1
