
def rev_string(s, i=1):
  if i > len(s):
    return ''
  return s[len(s)-i] + rev_string(s, i+1)

print('should reverse "porcupine". returned: ', rev_string('porcupine'), rev_string("porcupine") == 'enipucrop')