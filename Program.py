__author__ = 'Chris'

import abc
import Statement_Block

class Program(object):
    def __init__(self, block):
        assert isinstance(block, Statement_Block)
        if block is None:
            raise ValueError("null statement block argument")
        self.block = block

    @abc.abstractmethod
    def execute(self):
        self.block.Statement_Block.execute()