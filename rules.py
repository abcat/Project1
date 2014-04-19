#-*-coding:utf8-*-
"""This the Rule object"""
from handler import *


class Rule(object):
    """Base class for all rules"""
    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True


class HeadingRule(Rule):
    """A heading is a single line that is at most 70 characters and
    that doesn't end with a colon.
    """
    type = "title"
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self, block)


class TitleRule(HeadingRule):
    """
    The title is the first block in the document, provided that
    it is a heading
    """
    type = "title"
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self, block)


class ListItemrule(Rule):
    """
    A list item is a paragraph that begins with a hyphen. As part of
    the formating, the hyphen is removed.
    """

    type = "listitem"

    def condition(self, block):
        return block[0] == "-"

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip())
        handler.end(self.type)
        return True

class ListRule(ListItemrule):
    """A"""
