# A recursive function calls itself inside the function.   
def recursive_binary_search(list: list[int], target: int) ->bool:
  if len(list)==0:
    return False
  else:
    midpoint = len(list)//2

    if list[midpoint]==target:
      return True
    else:
      if list[midpoint]<target:
        return recursive_binary_search(list[midpoint+1:], target)
      return recursive_binary_search(list[:midpoint], target)

def verify(result):
  if result:
    print("Target found.")
  else:
    print("Target is not in the list")

nums = [0, 1, 5 , 9, 13, 17, 21, 27, 28, 33, 37]
result = recursive_binary_search(nums, 27)

verify(result)
