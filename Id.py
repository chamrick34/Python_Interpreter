__author__ = 'Chris'

from Arithmetic_Expression import Arithmetic_Expression
from Memory import Memory


class Id(Arithmetic_Expression):

    def __init__(self, char):
        if not char.isalpha():
            raise ValueError("invalid identifier")
        self.char = char

    def evaluate(self):
        return Memory.fetch(self.char)

    def get_char(self):
        return self.char