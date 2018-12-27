def find_index(arr, sub, i=0):
  if i >= len(arr):
    return -1
  elif arr[i] == sub:
    return i
  else:
    return find_index(arr, sub, i+1)

animals = ["duck", "cat", "pony"]

print(find_index(animals, 'duck'))
print(find_index(animals, "cat"))
print(find_index(animals, "pony"))
print(find_index(animals, "porcupine"))