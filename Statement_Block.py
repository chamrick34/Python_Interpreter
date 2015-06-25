__author__ = 'Chris'

import abc
from IllegalArgumentExceptions import IllegalArgumentException
from Statement_List import Statement_List

class Statement_Block(object):
    def __init__(self, stmts):
        if stmts is None:
            raise IllegalArgumentException("null statement list argument")
        assert isinstance(stmts, Statement_List)
        self.stmts = stmts

    @abc.abstractmethod
    def execute(self):
        for statement_lists in self.stmts:
            statement_lists.execute()