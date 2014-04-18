#-*-coding:utf8-*-
#!/usr/bin/env python
"""
This is Project 1 from 'Beginning Python-From Novice to Professional'
"""


def lines(file):
    """
    Read lines from file, and yield, make sure the last line of the file
    is empty.
    """
    for line in file:
        yield line
    yield "\n"


def blocks(file):
    """
    Yield blocks formed by lines, call lines(), pass the arguement file
    to lines().
    """
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line.strip())
            # print line
        elif block:
            #str.join method: the separator between elements is the string providing this method.
            yield " ".join(block).strip()
            block = []
