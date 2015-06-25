__author__ = 'Chris'

import abc
from Statement import Statement

class Print_Statement(Statement):
    def __init__(self, expr):
        if expr is None:
            raise ValueError("null arithmetic expression argument")
        self.expr = expr

    @abc.abstractmethod
    def execute(self):
        print(self.expr.evaluate())