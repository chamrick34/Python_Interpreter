__author__ = 'Chris'

from Arithmetic_Expression import Arithmetic_Expression
from Arithmetic_Operator import Arithmetic_Operator


class Binary_Expression(Arithmetic_Expression):

    def __init__(self, op, expr1, expr2):
        if expr1 is None or expr2 is None:
            raise ValueError("null expression argument")
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        if self.op == Arithmetic_Operator.ADD_OP:
            value = self.expr1.evaluate() + self.expr2.evaluate()
        elif self.op == Arithmetic_Operator.SUB_OP:
            value = self.expr1.evaluate() - self.expr2.evaluate()
        elif self.op == Arithmetic_Operator.DIV_OP:
            value = self.expr1.evaluate() / self.expr2.evaluate()
        elif self.op == Arithmetic_Operator.MUL_OP:
            value = self.expr1.evaluate() * self.expr2.evaluate()
        else:
            raise ValueError("invalid arithmetic operator")
        return value