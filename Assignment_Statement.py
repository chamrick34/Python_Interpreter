__author__ = 'Chris'

from Arithmetic_Expression import Arithmetic_Expression
from Statement import Statement
from Memory import Memory


class Assignment_Statement:

    def __init__(self, var, expr):
        if expr is None:
            raise ValueError("invalid expression argument")
        self.expr = expr
        if self.var is None:
            raise ValueError("Invalid variable argument")
        self.var = var

    def execute(self):
        self.var.setValue(self.expr.evaluate())
