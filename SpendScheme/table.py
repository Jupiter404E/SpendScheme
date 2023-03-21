"""

Copyright (C) 2022-2023 Jupiter404E.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2022-2023 present Jupiter404E
:license: MPL-2.0 license, see LICENSE for more details.

"""

__all__ = [
    'Table'
]

class Table:
            
    def createTable(
        data,
        cellUpper: str = None, 
        cellSep: str = None, 
        header_separator = None
    ) -> str:
        """
        An example of creating tables:
            >>> import SpendScheme
            >>> data = [['Product', 'Cost'],{'Strawberry': '2$','Blueberry':'2,71$','Banana':'1,63$','Apple':'30¢','Limon':'2$',}]
            >>> tableCreate = SpendScheme.Table()
            >>> print (tableCreate.createTable(data = data))
    
               Product |  Cost
            -----------+------
            Strawberry |    2$
             Blueberry | 2,71$
                Banana | 1,63$
                 Apple |   30¢
                 Limon |    2$
        """
        dataСount = [
            data[0]
        ]
        dataСount += [(k, v) for k, v in data[1].items()]

        rows = len(dataСount)
        cols = len(dataСount[0])

        cellU =  '-'  if cellUpper is None else cellUpper
        cellS = ' | ' if cellSep is None else ' {} '.format(cellSep)

        col_width = []
        for col in range(cols):
            columns = [str(dataСount[row][col]) for row in range(rows)]
            col_width.append(len(max(columns, key=len)))

        separator = '{}+{}'.format(cellU, cellU).join(cellU * n for n in col_width)

        lines = []

        for i, row in enumerate(range(rows)):
            result = []
            for col in range(cols):
                item = str(dataСount[row][col]).rjust(col_width[col])
                result.append(item)

            lines.append(cellS.join(result))

            if i == 0 and header_separator:
                lines.append(separator)

        return (
            '\n'.join(lines)
        )
