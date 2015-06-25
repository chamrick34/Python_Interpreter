__author__ = 'Chris'

import abc
from Arithmetic_Expression import Arithmetic_Expression

class Constant(Arithmetic_Expression):
    def __init__(self, value):
        self.value = value

    @abc.abstractmethod
    def evaluate(self):
        return self.value