
layers = ['|','¸','˛', '|', '.','◊', '.','=','/','∆','\\','~', '˘','†','¯','-','*','∏','ø','≈','<','<','','>','>']

colors = [
    '0;31;40m', # red
    '5;32;40m', # green flash
    '0;33;40m', # yellow    
    '5;34;40m', # blue flash
    '0;35;40m', # purple    
    '5;30;40m', # black flash
    '0;37;40m', # white
    '5;31;40m', # red flash
    '0;32;40m', # green
    '5;33;40m', # yellow flash  
    '0;34;40m', # blue
    '5;35;40m', # purple flash  
    '0;30;40m', # black flash
    '5;37;40m', # white flash
]

def set_color_scheme(text, color):
  return f'\x1b[{color}{text}\x1b[0m'

def tunnel(layers=[], size=None):
  if size == None:
    size = len(layers)
  if size % 2 == 0:
    size += 1
  if len(layers) < 1:
    layers = list(range(8))

  reversed_layers = list(reversed(layers))

  for row in range(size):
    x = row % len(layers)
    
    for col in range(size):
      y = col % len(layers)
      # if row+col>size-1:
      #   import pdb; pdb.set_trace()

      # this gives the top quadrant its shape
      layer_index = x

      # this gives the left quadrant its shape
      if row > col:
        layer_index = y

      # elif row > row-col:
      #   layer_index = ( len(layers)) - ( (row-1) % (len(layers) ) ) - 1
      
      # this gives the right quadrant its shape
      elif row+col>size-1:
        layer_index = ( len(layers)) - ( (col-1) % (len(layers) ) ) - 1


      
      try:   
        # this is where the indexing needs to change
        if col > size // 2:
          color = colors[layer_index%len(colors)]
          char = layers[ layer_index ]
        else:
          color = colors[ (layer_index%len(colors)) ]
          char = layers[layer_index]
      except IndexError:
        pass
        # print('index out of range', layer_index)

        
      # format color to char and space
      string = set_color_scheme(char, color)
      space = set_color_scheme('  ', color)

      # prints string without empty space instead of new line
      print(string, end=space)
    # print new line
    print('')


tunnel(layers, 50)
# tunnel(layers)
# tunnel(['0','-'])
# tunnel(['0','-'], 20)
