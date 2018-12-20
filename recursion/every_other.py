def every_other(s, i=0):
  if i >= len(s):
    return ''
  print(s[i], end='')
  return every_other(s, i+2)

def every_other2(s, i=0):
  if i >= len(s):
    return ''
  return s[i] + every_other2(s, i+2)

print('should print every other char')
every_other("hello")
print('')
print('should print every other char')
every_other("kevin")
print('')
print('should return every other char', every_other2("hello"), every_other2("hello") == 'hlo')
print('should return every other char', every_other2("kevin"), every_other2("kevin") == 'kvn')