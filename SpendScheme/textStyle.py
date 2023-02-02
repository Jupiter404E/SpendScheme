"""

    Copyright (C) 2022 Jupiter404E.

Text color list:
    black, red, green, yellow, blue, violet, cyan, white

Text style list:
    bold, italic, url, link, selected

"""

import os
import random

os.system("")

CSI = "\033["

def code_to_chars(code):
    return CSI + str(code) + "m"

class ColourCode(object):
    def __init__(self):
        for name in dir(self):
            if not name.startswith("_"):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))

class Colour(ColourCode):
    end    = 0
    black  = 30
    red    = 31
    green  = 32
    yellow = 33
    blue   = 34
    violet = 35
    cyan   = 36
    white  = 37

    random = random.randint(30, 37)
    
class ColourBG(ColourCode):
    end    = 0
    black  = 40
    red    = 41
    green  = 42
    yellow = 43
    blue   = 44
    violet = 45
    cyan   = 46
    white  = 37

    random = random.randint(40, 47)

class Style(ColourCode):
    end      = 0

    bold     = 1
    italic   = 3
    url      = 4
    link     = 5
    selected = 7

Color = Colour()
ColorBG = ColourBG()
