def binary_search(array, n, lo=0, hi=None):
  if hi is None:
      hi = len(array) - 1
  if lo > hi:
    return -1
  
  mid = (lo + hi) // 2

  if n == array[mid]:
    return mid
  if n < array[mid]:
    return binary_search(array, n, lo, mid-1)

  return binary_search(array, n, mid+1, hi)


print(binary_search([1,2,3,4], 1)) # 0
print(binary_search([1,2,3,4,5,6], 3)) # 2
print(binary_search([1,2,3,4], 5))# -1