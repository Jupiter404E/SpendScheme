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

class __Colour(ColourCode):
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

    def __List():
        for style in range(8):
            for fg in range(30, 38):
                s1 = ""
                for bg in range(40, 48):
                    format = ";".join([str(style), str(fg), str(bg)])
                    s1 += "\x1b[%sm %s \x1b[0m" % (format, format)
                print (
                    s1
                )
            print (
                "\033[0m \n"
            )

    list = __List()
    
class __ColourBG(ColourCode):
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

    def __List():
        for style in range(8):
            for fg in range(30, 38):
                s1 = ""
                for bg in range(40, 48):
                    format = ";".join([str(style), str(fg), str(bg)])
                    s1 += "\x1b[%sm %s \x1b[0m" % (format, format)
                print (
                    s1
                )
            print (
                "\033[0m \n"
            )

    list = __List()

class __Style(ColourCode):
    end      = 0

    bold     = 1
    italic   = 3
    url      = 4
    link     = 5
    selected = 7

Color = __Colour()
ColorBG = __ColourBG()
Style = __Style
