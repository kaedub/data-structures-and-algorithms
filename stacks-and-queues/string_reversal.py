from stack import Stack

def reverse_string(s):
  char_stack = Stack()
  for char in s:
    char_stack.push(char)

  reversed_string = ''
  while (char_stack.length > 0):
    reversed_string += char_stack.pop()
  return reversed_string

if __name__ == "__main__":
  print(reverse_string('hello'))
  print(reverse_string('goodbye'))