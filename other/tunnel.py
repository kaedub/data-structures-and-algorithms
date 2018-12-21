"""
0 0 0 0 0
0 1 1 1 0
0 1 0 1 0
0 1 1 1 0
0 0 0 0 0


[0,0] => [0,1] => [0,2] => [0,3] => [0,4] => [0,5]


[1,0] => [1,1] => [1,2] => [1,3] => [1,4] => [1,5]


[2,0] => [2,1] => [2,2] => [2,3] => [2,4] => [2,5]


[3,0] => [3,1] => [3,2] => [3,3] => [3,4] => [3,5]


[4,0] => [4,1] => [4,2] => [4,3] => [4,4] => [4,5]


    def __init__(self):    
        self.colors = COLORS[0: len(COLORS)]
        self.length = len(self.colors)    # = BOARD_WIDTH and BOARD_HEIGHT
        self.m = 0                          # m, movement
        self.direction = 1
        self.drawcross = False
        
    def draw_tunnel(self, status):
        m = 0
        if status == True:
            if self.direction == 1:
               self.m += 1
            elif self.direction == -1:
               self.m -= 1
        for i in range(BOARD_HEIGHT):
            ####################################################################
            # x and y hold data (color) positions, i and j hold matrix position
            # reflect: if halfway through list,
            #          then y = L - i - L - 1
            # L: length of layers
            # i: index for the row or column
            ####################################################################
            
            if i < self.length:
                y = i      
            else:
                y = self.length - (i - (self.length - 1))   		# reflect #
            
            for j in range(BOARD_WIDTH):
                self.rect[0] = ((CARD_WIDTH + GAP_SIZE) * j) + (GAP_SIZE / 2)
                if j < self.length:
                    x = j
                else:
                    x = self.length - (j - (self.length - 1))   	# reflect #
                    
                # x axis pattern logic

                limit = ((self.length * 2 - 1) - y)
                if (y <= j <= limit):     # pattern logic (y,x + t) % L
                    print(self.colors[ (y + self.m) % self.length ])                  
                else:
                    print(self.colors[ (x + self.m) % self.length ])



"""

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'




def tunnel(size, layers=[]):
  width = size
  height = width
  for row in range(width):
    x = row % len(layers)
    for col in range(height):
      y = col % len(layers)

      layer_index = x

      if row > col:
          layer_index = y
    
      # format color to char
      char = f'\x1b[{colors[layer_index%len(colors)]}{layers[layer_index]}\x1b[0m'

      space = f'\x1b[{colors[layer_index%len(colors)]} \x1b[0m'

      # prints char without empty space instead of new line
      print(char, end=space)
    # print new line
    print('')


layers = ['|','¸','˛', '|', '.','◊', '.','=','/','∆','\\','~', '˘','†','¯','-','*','∏','ø','≈','<','<','','>','>']

colors = [
    '0;31;40m', # red
    '5;32;40m', # green
    '0;33;40m', # yellow    
    '5;34;40m', # blue
    '0;35;40m', # purple    
    '5;30;40m', # black
    '0;37;40m', # white

    '5;31;40m', # red
    '0;32;40m', # green
    '5;33;40m', # yellow    
    '0;34;40m', # blue
    '5;35;40m', # purple    
    '0;30;40m', # black
    '5;37;40m', # white
]

# print('hello' + bcolors.OKBLUE)
# for color in colors:
#     print(f'\x1b[{color}' + 'Success!' + '\x1b[0m')

tunnel(40, layers)
