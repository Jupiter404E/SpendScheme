"""

Text style list:
    bold, italic, url, link, selected

"""

import os

os.system("")

class Style:
    def __init__(self):
        self.End      = "\33[0m"

        self.Bold     = "\33[1m"
        self.Italic   = "\33[3m"
        self.Url      = "\33[4m"
        self.Link     = "\33[5m"
        self.Selected = "\33[7m"

    def end(self):
        return (
            self.End
        )
    
    def bold(self):
        return (
            self.Bold
        )
    
    def italic(self):
        return (
            self.Italic
        )
    
    def url(self):
        return (
            self.Url
        )
    
    def link(self):
        return (
            self.Link
        )
    
    def selected(self):
        return (
            self.Selected
        )