__author__ = 'Chris'

import abc
from Statement import Statement


class Statement_List(object):
    def __init__(self):
        self.stmts = []

    def add(self, s):
        assert isinstance(s, Statement)
        self.stmts.append(s)

    @abc.abstractmethod
    def execute(self):
        for statement in self.stmts:
            statement.execute()