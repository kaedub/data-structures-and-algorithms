########################################
# Divide without using division, multiple, or modulo
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2

def divide(top, bot):
  if top == bot:
    return 1

  quotient = 0
  bot_inc = bot
  while (abs(bot_inc) < top):
    quotient += 1
    bot_inc += bot
  
  return quotient

print( divide(10, 3) )
print( divide(7, -3) ) 
print( divide(10, 10) )
print( divide(-7, 3) ) 