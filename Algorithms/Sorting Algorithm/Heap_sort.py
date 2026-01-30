# Time: O(nlogn), space: O(n) --> O(1) is possible
# to sort array in ascending order we make max heap and vice-versa
# We take an array --> heapify it -->

def heap_sort(nums: list[int]) -> list[int]:
  # making helper function(max_heapify), similar to shift-down function
  def max_heapify(nums: list[int], size_to_consider: int, starting_index: int) -> None:
    while True:
      largest = starting_index
      
      left = 2*starting_index + 1
      right = 2*starting_index + 2

      if left < size_to_consider and nums[left] > nums[largest]:
        largest = left
      if right < size_to_consider and nums[right] > nums[largest]:
        largest = right

      if largest==starting_index:
        break
      nums[largest], nums[starting_index] = nums[starting_index], nums[largest]
      starting_index = largest
    
  n = len(nums)
  # using max_heapify func on nums array
  for i in range(n//2 - 1, -1, -1):
    max_heapify(nums, n, i)

  # moving largest number in array(nums[0]) to end of array and repeating this
  for i in range(n-1, 0, -1):
    nums[0], nums[i] = nums[i], nums[0]
    max_heapify(nums, i, 0)
  
  return nums
