"""

    Copyright (C) 2022 Jupiter404E.

Text color list:
    black, red, green, yellow, blue, violet, cyan, white

Text style list:
    bold, italic, url, link, selected

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

class __Style(ColorCode):
    end      = "\33[0m"

    bold     = "\33[1m"
    italic   = "\33[3m"
    url      = "\33[4m"
    link     = "\33[5m"
    selected = "\33[7m"

Color = __Colour()
ColorBG = __ColourBG()
Style = __Style
