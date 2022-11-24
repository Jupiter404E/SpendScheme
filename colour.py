"""

"""

import os

os.system("")

'''class Color():
    END      = '\33[0m'
    BOLD     = '\33[1m'
    ITALIC   = '\33[3m'
    URL      = '\33[4m'
    LINK    = '\33[5m'
    LINK2   = '\33[6m'
    SELECTED = '\33[7m'

    BLACK  = '\33[30m'
    RED    = '\33[31m'
    GREEN  = '\33[32m'
    YELLOW = '\33[33m'
    BLUE   = '\33[34m'
    VIOLET = '\33[35m'
    BEIGE  = '\33[36m'
    WHITE  = '\33[37m'

    BLACKBG  = '\33[40m'
    REDBG    = '\33[41m'
    GREENBG  = '\33[42m'
    YELLOWBG = '\33[43m'
    BLUEBG   = '\33[44m'
    VIOLETBG = '\33[45m'
    BEIGEBG  = '\33[46m'
    WHITEBG  = '\33[47m'

    GREY    = '\33[90m'
    RED2    = '\33[91m'
    GREEN2  = '\33[92m'
    YELLOW2 = '\33[93m'
    BLUE2   = '\33[94m'
    VIOLET2 = '\33[95m'
    BEIGE2  = '\33[96m'
    WHITE2  = '\33[97m'
    MAGENTA = "\u001b[035m"

    GREYBG    = '\33[100m'
    REDBG2    = '\33[101m'
    GREENBG2  = '\33[102m'
    YELLOWBG2 = '\33[103m'
    BLUEBG2   = '\33[104m'
    VIOLETBG2 = '\33[105m'
    BEIGEBG2  = '\33[106m'
    WHITEBG2  = '\33[107m'

class DynamicColor():
    black_to_white = "\33[m;m;m"
    black_to_red = "\33[m;0;0"
    black_to_green = "\33[0;m;0"
    black_to_blue = "\33[0;0;m"

    white_to_black = "\33[n;n;n"
    white_to_red = "\33[255;n;n"
    white_to_green = "\33[n;255;n"
    white_to_blue = "\33[n;n;255"

    red_to_black = "\33[n;0;0"
    red_to_white = "\33[255;m;m"
    red_to_yellow = "\33[255;m;0"
    red_to_purple = "\33[255;0;m"

    green_to_black = "\33[0;n;0"
    green_to_white = "\33[m;255;m"
    green_to_yellow = "\33[m;255;0"
    green_to_cyan = "\33[0;255;m"

    blue_to_black = "\33[0;0;n"
    blue_to_white = "\33[m;m;255"
    blue_to_cyan = "\33[0;m;255"
    blue_to_purple = "\33[m;0;255"

    yellow_to_red = "\33[255;n;0"
    yellow_to_green = "\33[n;255;0"

    purple_to_red = "\33[255;0;n"
    purple_to_blue = "\33[n;0;255"

    cyan_to_green = "\33[0;255;n"
    cyan_to_blue = "\33[0;n;255"'''

class Colour:
    def __init__(self):
        self.End      = '\33[0m'

        self.Black  = '\33[30m'
        self.Red    = '\33[31m'
        self.Green  = '\33[32m'
        self.Yellow = '\33[33m'
        self.Blue   = '\33[34m'
        self.Violet = '\33[35m'
        self.Cyan  = '\33[36m'
        self.White  = '\33[37m'
        """
        BLACKBG  = '\33[40m'
        REDBG    = '\33[41m'
        GREENBG  = '\33[42m'
        YELLOWBG = '\33[43m'
        BLUEBG   = '\33[44m'
        VIOLETBG = '\33[45m'
        BEIGEBG  = '\33[46m'
        WHITEBG  = '\33[47m'

        GREY    = '\33[90m'
        RED2    = '\33[91m'
        GREEN2  = '\33[92m'
        YELLOW2 = '\33[93m'
        BLUE2   = '\33[94m'
        VIOLET2 = '\33[95m'
        BEIGE2  = '\33[96m'
        WHITE2  = '\33[97m'
        MAGENTA = "\u001b[035m"

        GREYBG    = '\33[100m'
        REDBG2    = '\33[101m'
        GREENBG2  = '\33[102m'
        YELLOWBG2 = '\33[103m'
        BLUEBG2   = '\33[104m'
        VIOLETBG2 = '\33[105m'
        BEIGEBG2  = '\33[106m'
        WHITEBG2  = '\33[107m'"""

    def end(self):
        return (
            self.End
        )
    
    def black(self):
        return (
            self.Black
        )
    
    def red(self):
        return (
            self.Red
        )
    
    def green(self):
        return (
            self.Green
        )
    
    def green(self):
        return (
            self.Green
        )
    
    def yellow(self):
        return (
            self.Yellow
        )
    
    def blue(self):
        return (
            self.Blue
        )
    
    def violet(self):
        return (
            self.Violet
        )
    
    def cyan(self):
        return (
            self.Cyan
        )
    
    def white(self):
        return (
            self.White
        )