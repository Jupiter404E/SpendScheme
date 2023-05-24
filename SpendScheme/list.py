"""

Copyright (C) 2022-2023 Jupiter404E.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2022-2023 present Jupiter404E
:license: MPL-2.0 license, see LICENSE for more details.

"""

from math import ceil

__all__ = [
    'List'
]

class List:

    __slots__ = (
        'list'
    )
    
    def __init__(self, list: list):
        """
        Parameters
        ----------
            :param list: `list` list.
        """
        self.list = list

    def autoList(self):
        """Create an auto list.

        Usage
        -----
            >>> list = ["Apple", "Banana", "Milk", "Coconat"]
            >>> auto_list = SpendScheme.List(list)
            >>> auto_list.autoList()
    
            0. Apple
            1. Banana
            2. Milk
            3. Coconat
        """
        index = 0

        while index < len(self.list):
            print('{}. '.format(index) + self.list[index])
            index = index + 1

    def chunk(self, size):
        """Usage chunk.

        Usage
        -----
            >>> chunk_list = SpendScheme.List([1, 2, 3, 4, 5, 6, 7, 8]) # List.
            >>> chunk_list = chunk_list.chunk(2) # Chunk size value.
            >>> print(chunk_list)

            [[1, 2], [3, 4], [5, 6], [7, 8]]

        Parameters
        ----------
            :param size: Chunk size value.
        """
        return list(map(lambda x: self.list[x * size:x * size + size],
                list(range(0, ceil(len(self.list) / size)))))
