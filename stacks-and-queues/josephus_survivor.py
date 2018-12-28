# Imagine a group of 10 people in a circle, numbered 1 to 10. 
# If we started at the first person (#1) and killed every three people, 
# it would look like this:
#
# 1  2  3  4  5  6  7  8  9  10
#       !        !        !
#
# This continues, though, looping around again, starting with where we left off 
# at #10 
#
# 1  2  3  4  5  6  7  8  9  10
#    !  X        X  !     X
#
# And again, starting where that left off, at #8, and continuing:
#
# 1  2  3  4  5  6  7  8  9  10
# !  X  X        X  X  !  X
#
# 1  2  3  4  5  6  7  8  9  10
# X  X  X     !  X  X  X  X
#
# 1  2  3  4  5  6  7  8  9  10
# X  X  X     X  X  X  X  X  !
#

def josephus_survivor(people):
  circle = create_circular_list(people)

def create_circular_list(items):
  pass
  # for item in items: