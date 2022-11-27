"""

    Copyright (C) 2022 Jupiter404E.

"""

class Formatting():

    __slots__ = (
        "text"
    )

    def __init__(
        self,
        *,
        text = None,
    ):
        if text is not None:
            self.text = text

        elif text is None:
            self.text = "None"

    def lowerTranslit(self):    
        self.text = str(self.text).lower()

    def answer(
        self,
        color = None
    ):
        if color is not None:
            return (
                    color + self.text + "\33[0m"
            )
        
        else:
            return (
                    self.text
            ) 
