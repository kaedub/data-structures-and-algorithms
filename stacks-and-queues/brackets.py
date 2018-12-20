from stack import Stack

OPEN_CHARS = {'{', '(', '['}
CLOSE_CHARS = {'}', ')', ']'}

def is_balanced(s):
  open = False
  stack = Stack()
  for char in s:
    if char in CLOSE_CHARS and not open:
      return False
    if char in CLOSE_CHARS:
      previous = stack.pop()
      # print('popped from stack', previous)
      while (previous not in OPEN_CHARS):
        previous = stack.pop()
      if stack.length < 1:
        open = False
    if char in OPEN_CHARS:
      open = True
    if open:
      # print('pushing to stack', char)
      stack.push(char)
  # print(stack, stack.length)
  return True if stack.length < 1 else False
    
if __name__ == "__main__":
  print('(hi [there])', is_balanced('(hi [there])'))
  print('ab(cd(ef)g)h[i]j{k}', is_balanced('ab(cd(ef)g)h[i]j{k}'))
  print('ab(cd(ef)g)h[i]j{k', is_balanced('ab(cd(ef)g)h[i]j{k'))
  print('(hi) [there]', is_balanced('(hi) [there]'))
  print('hello', is_balanced('hello'))
  print('hello)', is_balanced('hello)'))