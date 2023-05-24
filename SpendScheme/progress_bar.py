"""

Copyright (C) 2022-2023 Jupiter404E.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2022-2023 present Jupiter404E
:license: MPL-2.0 license, see LICENSE for more details.

"""

def progress_bar(
        iteration: int,
        total: int,
        prefix: str,
        suffix: str,
        decimals: int = None,
        length: int = None,
        fill: str = "█"
    ):
    """Create a progress bar.

    Usage
    -----
        >>> import time
        >>> for i in range(100):
        >>>     time.sleep(0.1)
        >>>     progress_bar(
        >>>         i + 1, 100, prefix="Prefix:", suffix="Complete")

    Parameters
    ----------
        :param iteration: `int` Current progress step.
        :param total: `int` Total number of progress steps.
        :param prefix: `str` Prefix for the progress bar text.
        :param suffix: `str` Suffix for the progress bar text.
        :param decimals: `int` The number of decimal places (for the percent complete value).
        :param length: `int` Progress bar string length.
        :param fill: `str` Symbol for filling the progress bar.
    """
    length = 100 if length is None else length
    decimals = 1 if decimals is None else decimals

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + "-" * (length - filled_length)
    print(f"\r{prefix} |{bar}| {percent}%", end="\r") # {suffix}
    if iteration == total:
        print()
