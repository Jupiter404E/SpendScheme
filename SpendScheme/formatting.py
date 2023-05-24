"""

Copyright (C) 2022-2023 Jupiter404E.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2022-2023 present Jupiter404E
:license: MPL-2.0 license, see LICENSE for more details.

"""

from typing import Any

def prettyText(
        value,
        style = None
    ) -> Any:
        
        """
        Usage
        -----
            >>> prettyText("Hello world!", (Color.green))

        Parameters
        ----------
            :param value: Values.
            :param style: Text style.
        """
        
        value = str(value)

        if style:
            for styles in style:
                style = styles
                value = str(style + value + "\33[0m")

        return value
