__author__ = 'Chris'


class Token(object):

    def __init__(self, lexeme, rowNum, colNum, tok):
        '''

        :param lexeme: cannot be empty/null
        :param rowNum: must be >= 1
        :param colNum: must be >= 1

        '''
        if lexeme is None or len(lexeme) == 0:
            raise ValueError("invalid lexeme argument")
        if rowNum < 1:
            raise ValueError("invalid row number argument")
        if colNum < 1:
            raise ValueError("invalid column number argument")
        self.lexeme = lexeme
        self.rowNum = rowNum
        self.colNum = colNum
        self.tok = tok

    def get_lexeme(self):
        return self.lexeme

    def get_row_number(self):
        return self.rowNum

    def get_column_number(self):
        return self.colNum

    def get_token_type(self):
        return self.tok

    def __str__(self):
        return "{0}: {1:<5}, row: {2:<5}, column: {3:<5}".format(self.tok, self.lexeme, self.rowNum, self.colNum)