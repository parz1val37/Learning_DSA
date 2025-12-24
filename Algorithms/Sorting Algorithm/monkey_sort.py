# Randomly shuffling the array until it gets sorted
from random import shuffle as shuffle

def is_sorted(arr):
  for i in range(len(arr)):
    if arr[i]>arr[i+1]:
      return False
  return True
    
def monkey_sort(arr):
  while not is_sorted(arr):
    shuffle(arr)
  return arr
