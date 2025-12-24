''' Time complexity: O(n²)
    Space complexity: O(1)'''

# Not Adaptive
# Not Stable

def selection_sort(arr):
  for i in range(len(arr)-1):
    min = i

    for j in range(i+1, len(arr)):
      if arr[j] < arr[min]:
        min = j
    arr[i],arr[min] = arr[min],arr[i]
  return arr
