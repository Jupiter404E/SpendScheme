"""

Text color list:
    black, red, green, yellow, blue, violet, cyan, white

"""

import os

os.system("")

class Colour:
    def __init__(self):
        self.End      = "\33[0m"

        self.Black  = "\33[30m"
        self.Red    = "\33[31m"
        self.Green  = "\33[32m"
        self.Yellow = "\33[33m"
        self.Blue   = "\33[34m"
        self.Violet = "\33[35m"
        self.Cyan  = "\33[36m"
        self.White  = "\33[37m"

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
    
class ColourBG:
    def __init__(self):
        self.End      = "\33[0m"

        self.BlackBG  = "\33[40m"
        self.RedBG    = "\33[41m"
        self.GreenBG  = "\33[42m"
        self.YellowBG = "\33[43m"
        self.BlueBG   = "\33[44m"
        self.VioletBG = "\33[45m"
        self.CyanBG   = "\33[47m"
        self.WhiteBG  = "\33[37m"

    def end(self):
        return (
            self.End
        )
    
    def black(self):
        return (
            self.BlackBG
        )
    
    def red(self):
        return (
            self.RedBG
        )
    
    def green(self):
        return (
            self.GreenBG
        )
    
    def green(self):
        return (
            self.YellowBG
        )
    
    def yellow(self):
        return (
            self.YellowBG
        )
    
    def blue(self):
        return (
            self.BlueBG
        )
    
    def violet(self):
        return (
            self.VioletBG
        )
    
    def cyan(self):
        return (
            self.CyanBG
        )
    
    def white(self):
        return (
            self.WhiteBG
        )