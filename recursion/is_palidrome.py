def is_palindrome(s, i=0):
  if i >= len(s)/2:
    return True
  if s[i] != s[len(s)-i-1]:
    return False
  else:
    return is_palindrome(s, i+1)

print('should return true', is_palindrome("tacocat"))
print('should return true', is_palindrome("racecar"))
print('should return true', is_palindrome("raceecar"))
print('should return true', is_palindrome(""))
print('should return false', is_palindrome("race"))
print('should return false', is_palindrome("tacodog"))