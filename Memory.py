__author__ = 'Chris'


class Memory(object):

    mem = dict()

    def __init__(self):
        '''
        constructor
        '''

    def store(self, var, value):
        if not var.isalpha():
            raise RuntimeError("invalid memory access")
        val = value.lower()
        self.mem[var] = val

    def fetch(self, variable):
        if not variable.isalpha():
            raise RuntimeError("invalid memory access")
        var1 = variable.lower()
        return self.mem[var1]