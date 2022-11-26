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

    def Table(self, data, cell_sep=' | ', header_separator = True) -> str:
        dataСount = [
            data[0]
        ]
        dataСount += [(k, v) for k, v in data[1].items()]

        rows = len(dataСount)
        cols = len(dataСount[0])

        col_width = []
        for col in range(cols):
            columns = [str(dataСount[row][col]) for row in range(rows)]
            col_width.append(len(max(columns, key=len)))

        separator = "-+-".join('-' * n for n in col_width)

        lines = []

        for i, row in enumerate(range(rows)):
            result = []
            for col in range(cols):
                item = str(dataСount[row][col]).rjust(col_width[col])
                result.append(item)

            lines.append(cell_sep.join(result))

            if i == 0 and header_separator:
                lines.append(separator)

        return (
                '\n'.join(lines)
        )