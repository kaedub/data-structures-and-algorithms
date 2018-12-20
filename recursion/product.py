def product(nums, acc=1):
  if len(nums) < 1:
    return acc
  acc *= nums.pop()
  return product(nums, acc)

print('should return product of [2,3,4]', product([2, 3, 4]), product([2,3,4]) == 24)
print('should return product of [4,2,2]', product([4, 2, 2]), product([4,2,2]) == 12)