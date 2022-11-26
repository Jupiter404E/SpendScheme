"""

    Copyright (C) 2022 Jupiter404E.

"""

class Table():

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
            
    def createTable(self, data, cellUpper = None, cellSep = None, header_separator = True) -> str:
        dataСount = [
            data[0]
        ]
        dataСount += [(k, v) for k, v in data[1].items()]

        rows = len(dataСount)
        cols = len(dataСount[0])

        cellU = "-" if cellUpper is None else cellUpper
        cellS = " | " if cellSep is None else " {} ".format(cellSep)

        col_width = []
        for col in range(cols):
            columns = [str(dataСount[row][col]) for row in range(rows)]
            col_width.append(len(max(columns, key=len)))

        separator = "{}+{}".format(cellU, cellU).join(cellU * n for n in col_width)

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
