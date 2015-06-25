__author__ = 'Chris'

from Statement import Statement

class If_Statement(Statement):

    def __init__(self):
        self.exprList = list()
        self.blockList = list()

    def add_expression(self, expr):
        if expr is None:
            raise ValueError("Invalid expression argument")
        self.exprList.append(expr)

    def add_block(self, block):
        self.blockList.append(block)

    def execute(self):
        if self.blockList.__len__() == 0:
            raise RuntimeError("illegal If Statement")
        if self.exprList.__len__() + 1 != self.blockList.__len__():
            raise RuntimeError("illegal If Statement")
        i = 0
        while i < self.exprList.__len__() and not self.exprList.__getitem__(i).evaluate():
            i += 1
        if i < self.exprList.__len__():
            self.blockList.__getitem__(i).execute()
        else:
            self.blockList.__getitem__(self.blockList.__len__() - 1).execute()