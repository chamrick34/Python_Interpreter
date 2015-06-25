__author__ = 'Chris'

from Relational_Operator import Relational_Operator

class Boolean_Expression(object):

    def __init__(self, op, expr1, expr2):
        if expr1 is None or expr2 is None:
            raise ValueError("Invalid expression argument")
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        if self.op == Relational_Operator.LE_OP:
            value = self.expr1.evaluate() <= self.expr2.evaluate()
        elif self.op == Relational_Operator.EQ_OP:
            value = self.expr1.evaluate() == self.expr2.evaluate()
        elif self.op == Relational_Operator.GE_OP:
            value = self.expr1.evaluate() >= self.expr2.evaluate()
        elif self.op == Relational_Operator.GT_OP:
            value = self.expr1.evaluate() > self.expr2.evaluate()
        elif self.op == Relational_Operator.LT_OP:
            value = self.expr1.evaluate() < self.expr2.evaluate()
        elif self.op == Relational_Operator.NE_OP:
            value = self.expr1.evaluate() != self.expr2.evaluate()
        else:
            raise ValueError("invalid relational operator")
        return value