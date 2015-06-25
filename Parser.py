__author__ = 'Chris'

from Lexical_Analyzer import Lexical_Analyzer
from Lexical_Exception import LexicalException
from Parser_Exception import ParserException
from Statement_Block import Statement_Block
from If_Statement import If_Statement
from Statement_List import Statement_List
from Statement import Statement
from Print_Statement import Print_Statement
from While_Statement import While_Statement
from Token import  Token
from TokenTypes import TokenType
from Arithmetic_Operator import Arithmetic_Operator
from Relational_Operator import Relational_Operator
from Constant import Constant
from Id import Id
from Binary_Expression import Binary_Expression
from Boolean_Expression import  Boolean_Expression
from Program import Program
from Assignment_Statement import  Assignment_Statement

class Parser(object):

    def __init__(self, fileName):
        self.lex = Lexical_Analyzer.__new__(fileName)

    def parse(self):
        tok = self.get_next_token()
        self.match(tok, TokenType.MAIN_TOK)
        tok = self.get_next_token()
        self.match(tok, TokenType.LEFT_PAREN_TOK)
        tok = self.get_next_token()
        self.match(tok, TokenType.RIGHT_PAREN_TOK)
        tok = self.get_next_token()
        self.match(tok, TokenType.EOLN_TOK)
        block = self.get_statement_block()
        tok = self.get_next_token()
        if tok.Token.get_token_type() != TokenType.EOS_TOK:
            raise ParserException("invalid end of file")
        return Program(block)


    def get_statement_block(self):
        tok = self.get_next_token()
        self.match(tok, TokenType.INDENT_TOK)
        stmts = self.get_statement_list()
        tok = self.get_next_token()
        self.match(tok, TokenType.DEDENT_TOK)
        return Statement_Block.__new__(stmts)


    def get_statement_list(self):
        stmts = Statement_List()
        s = self.get_statement()
        stmts.add(s)
        tok = self.get_look_ahead_token()
        while self.is_valid_start_of_statement(tok):
            s = self.get_statement()
            stmts.add(s)
            tok = self.get_look_ahead_token()
        return stmts


    def is_valid_start_of_statement(self, tok):
        if tok.Token.get_token_type() == TokenType.PRINT_TOK or tok.Token.get_token_type() == TokenType.ID_TOK or tok.Token.get_token_type() == TokenType.WHILE_TOK or tok.Token.get_token_type() == TokenType.IF_TOK:
            return True
        else:
            return False


    def get_statement(self):
        s = Statement()
        tok = self.get_look_ahead_token()
        if tok.Token.get_token_type() == TokenType.PRINT_TOK:
            s = self.get_print_statement()
        elif tok.Token.get_token_type() == TokenType.IF_TOK:
            s = self.get_if_statement()
        elif tok.Token.get_token_type() == TokenType.WHILE_TOK:
            s = self.get_while_statement()
        else:
            s = self.get_assignment_statement()
        return s


    def get_assignment_statement(self):
        var = self.get_id()
        tok = self.get_next_token()
        self.match(tok, TokenType.ASSIGN_TOK)
        expr = self.get_arithmetic_expression()
        tok = self.get_next_token()
        self.match(tok, TokenType.EOLN_TOK)
        return Assignment_Statement.__new__(var, expr)


    def get_while_statement(self):
        tok = self.get_next_token()
        self.match(tok, TokenType.WHILE_TOK)
        expr = self.get_boolean_expression()
        tok = self.get_next_token()
        self.match(tok, TokenType.COLON_TOK)
        tok = self.get_next_token()
        self.match(tok, TokenType.EOLN_TOK)
        block = self.get_statement_block()
        return While_Statement.__new__(expr, block)

    def get_if_statement(self):
        s = If_Statement()
        tok = self.get_next_token()
        self.match(tok, TokenType.IF_TOK)
        expr = self.get_boolean_expression()
        s.add_expression(expr)
        tok = self.get_next_token()
        self.match(tok, TokenType.COLON_TOK)
        tok = self.get_next_token()
        self.match(tok, TokenType.EOLN_TOK)
        block = self.get_statement_block()
        s.add_block(block)
        tok = self.get_next_token()

        while tok.Token.get_token_type() == TokenType.ELIF_TOK:
            self.match(tok, TokenType.ELIF_TOK)
            expr = self.get_boolean_expression()
            s.add_expression(expr)
            tok = self.get_next_token()
            self.match(tok, TokenType.COLON_TOK)
            tok = self.get_next_token()
            self.match(tok, TokenType.EOLN_TOK)
            block = self.get_statement_block()
            s.add_block(block)
            tok = self.get_next_token()

        self.match(tok, TokenType.ELSE_TOK)
        tok = self.get_next_token()
        self.match(tok, TokenType.COLON_TOK)
        tok = self.get_next_token()
        self.match(tok, TokenType.EOLN_TOK)
        block = self.get_statement_block()
        s.add_block(block)
        return s



    def get_print_statement(self):
        tok = self.get_next_token()
        self.match(tok, TokenType.PRINT_TOK)
        tok = self.get_next_token()
        self.match(tok, TokenType.LEFT_PAREN_TOK)
        expr = self.get_arithmetic_expression()
        tok = self.get_next_token()
        self.match(tok, TokenType.RIGHT_PAREN_TOK)
        tok = self.get_next_token()
        self.match(tok, TokenType.EOLN_TOK)
        return Print_Statement.__new__(expr)


    def get_boolean_expression(self):
        op = self.get_relational_operator()
        expr1 = self.get_arithmetic_expression()
        expr2 = self.get_arithmetic_expression()
        return Boolean_Expression.__new__(op, expr1, expr2)


    def get_arithmetic_expression(self):
        tok = self.get_look_ahead_token()
        if tok.Token.get_token_type() == TokenType.ID_TOK:
            expr = self.get_id()
        elif tok.Token.get_token_type() == TokenType.CONST_TOK:
            expr = self.get_literal_constant()
        else:
            op = self.get_arithmetic_operator()
            expr1 = self.get_arithmetic_expression()
            expr2 = self.get_arithmetic_expression()
            expr = Binary_Expression.__new__(op, expr1, expr2)
        return expr


    def get_literal_constant(self):
        tok = self.get_next_token()
        self.match(tok, TokenType.CONST_TOK)
        value = tok.Token.get_lexeme()
        return Constant.__new__(value)


    def get_relational_operator(self):
        tok = self.get_next_token()
        if tok.Token.get_token_type() == TokenType.EQ_TOK:
            op = Relational_Operator.EQ_OP
        if tok.Token.get_token_type() == TokenType.NE_TOK:
            op = Relational_Operator.NE_OP
        if tok.Token.get_token_type() == TokenType.LE_TOK:
            op = Relational_Operator.LE_OP
        if tok.Token.get_token_type() == TokenType.LT_TOK:
            op = Relational_Operator.LT_OP
        if tok.Token.get_token_type() == TokenType.GT_TOK:
            op = Relational_Operator.GT_OP
        if tok.Token.get_token_type() == TokenType.GE_TOK:
            op = Relational_Operator.GE_OP
        else:
            raise ParserException("relational operator expected")
        return op

    def get_arithmetic_operator(self):
        tok = self.get_next_token()
        if tok.Token.get_token_type() == TokenType.ADD_TOK:
            op = Arithmetic_Operator.ADD_OP
        if tok.Token.get_token_type() == TokenType.SUB_TOK:
            op = Arithmetic_Operator.SUB_OP
        if tok.Token.get_token_type() == TokenType.MUL_TOK:
            op = Arithmetic_Operator.MUL_OP
        if tok.Token.get_token_type() == TokenType.DIV_TOK:
            op = Arithmetic_Operator.DIV_OP
        else:
            raise ParserException("arithmetic operator expected")
        return op


    def get_id(self):
        tok = self.get_next_token()
        self.match(tok, TokenType.ID_TOK)
        return Id.__new__(tok.Token.get_lexeme()[0])


    def match(self, tok, tokType):
        if tok.Token.get_token_type() != tokType:
            raise ParserException(str(tokType) + "expected at row " + str(tok.Token.get_row_number()) + " and column "
                                  + str(tok.Token.get_column_number()))

    def get_look_ahead_token(self):
        try:
            tok = self.lex.get_look_ahead_token()
        except LexicalException:
            raise ParserException("no more tokens")
        return tok

    def get_next_token(self):
        try:
            tok = self.lex.get_next_token()
        except LexicalException:
            raise ParserException("no more tokens")
        return tok


