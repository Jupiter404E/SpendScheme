"""

Text color list:
    black, red, green, yellow, blue, violet, cyan, white

"""

import os

os.system("")

CSI = '\033['

def code_to_chars(code):
    return CSI + str(code) + 'm'

class ColorCode(object):
    def __init__(self):
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))

class __Colour(ColorCode):
    end = 0
    black = 30
    red = 31
    green = 32
    yellow = 33
    blue = 34
    violet = 35
    cyan = 37
    white = 37
    
class __ColourBG(ColorCode):
    end = 0
    black = 40
    red = 41
    green = 42
    yellow = 43
    blue = 44
    violet = 45
    cyan = 47
    white = 37
    
Color = __Colour()
ColorBG = __ColourBG()
