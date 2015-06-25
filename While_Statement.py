__author__ = 'Chris'

import abc
from Statement import Statement

class While_Statement(Statement):
    def __init__(self, expr, block):
        if expr is None:
            raise ValueError("Illegal expression argument")
        if block is None:
            raise ValueError("Illegal statement block argument")
        self.expr = expr
        self.block = block

    @abc.abstractmethod
    def execute(self):
        while self.expr.evaluate():
            self.block.execute()