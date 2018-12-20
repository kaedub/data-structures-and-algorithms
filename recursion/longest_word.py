def longest_word(words, i=0, longest=0):
  if i >= len(words):
    return longest
  if longest < len(words[i]):
    longest = len(words[i])
  return longest_word(words, i+1, longest)

print('should return length of longest word', longest_word(["hello", "hi", "hola"]) == 5)
print('should return length of longest word', longest_word(["oligarchy", "hello", "bonjour"]) == 9)