# Space Complexity: constant

'''Adaptive Sort: A sorting algorithm falls into the adaptive sort family if it 
  takes advantage of existing order in its input. It benefits from the presortedness 
  in the input sequence - or a limited amount of disorder for various
  definitions of measures of disorder - and sorts faster. Adaptive sorting is 
  usually performed by modifying existing sorting algorithms.'''

'''Stable Algorithm: A sorting algorithm is said to be stable if two objects with equal keys
  appear in the same order in sorted output as they appear in the input array
  to be sorted. Some sorting algorithms are stable by nature like 
  Insertion sort, Merge Sort, Bubble Sort, etc. And some sorting algorithms are 
  not, like - Heap Sort, Quick Sort, etc.
'''

# Bubble sort without adaptation
# Time Complexity: Big(O) of n² 
def bubble_sort(arr):
  for i in range(len(arr) - 1):
    for j in range(len(arr) -1 - i):
      if arr[j]> arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
  return arr

arr = [6, 35, 2, 7, 9, 3]
print(bubble_sort(arr))

# Bubble sort with adaptation
# Best case time complexity: Big(O) of n
def bubble_sort_adaptive(arr):
  for i in range(len(arr) - 1):
    flag = 0
    for j in range(len(arr) -1 - i):
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]
        flag = 1
    if flag == 0:
      break
  return arr
