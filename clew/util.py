
from time import localtime, strftime


def verbosity(text, silent, include_time=True, newline=True):
    if silent:
        return
    current_time = str()
    if include_time:
        current_time = strftime("%Y-%m-%d %H:%M:%S ", localtime()) + ': '

    if newline:
        print(current_time + text)
    else:
        print(current_time + text, end='')