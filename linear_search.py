def linear_search(list, target):
  '''
  Returns the index position of the target if found, else returns None
  '''
  
  for i in range(0, len(list)):
    if list[i] == target:
      return i
  return None 

def verify(index):
  if index is not None:
    print("Target found at index: ", index)
  else:
    print("Target not found in list")

numbers = [10,20,30,40,50,60,70,80,90,100]

results = linear_search(numbers, 120)
verify(results)

results = linear_search(numbers, 60)
verify(results)
