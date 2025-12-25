# Time complexity: O(nlog(n)), Space complexity: O(n)

# Not Adaptive
# Stable

# Function to join the two sorted array.
# It will be helper function for merge sort algorithm.
def merge_sorted(arr1, arr2, arr):
  i = j = k = 0

  while (i<len(arr1)) and (j<len(arr2)):
    if arr2[j]<arr1[i]:
      arr[k]=arr2[j]
      j += 1
    
    else:
      arr[k] = arr1[i]
      i += 1
    k += 1

  '''After the end of 'while loop' some item of either one of these two arrays will remain,
  so now simply adding these remaining items as individual arrays are sorted.''' 
  while i < len(arr1):
    arr[k] = arr1[i]
    i += 1
    k += 1
  while j < len(arr2):
    arr[k] = arr2[j]
    j += 1
    k += 1

def merge_sort(arr):
  if len(arr) == 1:
    return arr
  
  left = arr[len(arr)//2:]
  right = arr[:len(arr)//2]

  merge_sort(left)
  merge_sort(right)

  merge_sorted(left, right, arr)  

if __name__ == '__main__':
  arr = [5, -3, 3, 78, 1, -7]
  merge_sort(arr)
  print(arr)
