"""

Copyright (C) 2022-2023 Jupiter404E.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2022-2023 present Jupiter404E
:license: MPL-2.0 license, see LICENSE for more details.

"""

__all__ = [
    'List'
]

class List:

    __slots__ = (
        'list'
    )
    
    def __init__(self, list: list):
        self.list = list

    def autoList(self):
        """
        An example of creating automatics lists:
            >>> import SpendScheme
            >>> list = ["Apple", "Banana", "Milk", "Coconat"]
            >>> SS = SpendSchemeTest.List(list = list)
            >>> SS.autoList()
    
            0. Apple
            1. Banana
            2. Milk
            3. Coconat
        """
        index = 0

        while index < len(self.list):
            print('{}. '.format(index) + self.list[index])
            index = index + 1
