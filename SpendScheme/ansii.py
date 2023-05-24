"""

Copyright (C) 2022-2023 Jupiter404E.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2022-2023 present Jupiter404E
:license: MPL-2.0 license, see LICENSE for more details.

"""

import os
import random

os.system("")

CSI = '\033['

__all__ = [
    'Colour',
    'Color',
    'ColourBG',
    'ColorBG',
    'Style',
    'code_to_chars'
]

def code_to_chars(code):
    """Code to chars.

    Parameters
    ----------
        :param code: Code.
    """
    return CSI + str(code) + 'm'

class ColourCode(object):
    def __init__(self):
        for name in dir(self):
            if not name.startswith('_'):
                value = getattr(self, name)
                setattr(self, name, code_to_chars(value))

class Colour(ColourCode):
    """Usage colors.

    Usage
    -----
        - `Color.color_name`

    Colors
    ------
        - `end`
        - `black or light_black`
        - `red or light_red`
        - `green or light_green`
        - `yellow or light_yellow`
        - `blue or light_blue`
        - `violet or light_violet`
        - `cyan or light_cyan`
        - `white or light_white`
        - `random`
    """

    end    = 0
    black  = 30
    red    = 31
    green  = 32
    yellow = 33
    blue   = 34
    violet = 35
    cyan   = 36
    white  = 37

    # Many terminals may not support the colors below

    light_black   = 90
    light_red     = 91
    light_green   = 92
    light_yellow  = 93
    light_blue    = 94
    light_violet  = 95
    light_cyan    = 96
    light_white   = 97

    random = random.choice([random.randint(30, 37), random.randint(90, 97)])

class ColourBG(ColourCode):
    """Usage backgrounds colors.

    Usage
    -----
        - `ColorBG.color_name`

    Colors
    ------
        - `end`
        - `black or light_black`
        - `red or light_red`
        - `green or light_green`
        - `yellow or light_yellow`
        - `blue or light_blue`
        - `violet or light_violet`
        - `cyan or light_cyan`
        - `white or light_white`
        - `random`
    """

    end    = 0
    black  = 40
    red    = 41
    green  = 42
    yellow = 43
    blue   = 44
    violet = 45
    cyan   = 46
    white  = 47

    # Many terminals may not support the colors below

    light_black   = 100
    light_red     = 101
    light_green   = 102
    light_yellow  = 103
    light_blue    = 104
    light_violet  = 105
    light_cyan    = 106
    light_white   = 107

    random = random.choice([random.randint(30, 37), random.randint(100, 107)])

class Style_(ColourCode):
    """Usage styles.

    Usage
    -----
        - `Style.style_name`

    Styles
    ------
        - `bold`
        - `italic`
        - `url`
        - `link`
        - `selected`
    """
    end      = 0

    bold     = 1
    italic   = 3
    url      = 4
    link     = 5
    selected = 7

Color = Colour()
ColorBG = ColourBG()
Style = Style_()
