__author__ = 'Chris'

from Lexical_Exception import LexicalException
from Token import Token
from TokenTypes import TokenType


class Lexical_Analyzer(object):

    def __init__(self, fileName):
        if fileName is None:
            raise ValueError("null file argument")
        input_file = open(fileName, "r")
        lineNum = 0
        indention = 0
        self.tokenList = list()
        for line in iter(input_file):
            lineNum += 1
            numTabs = self.find_num_preceding_tabs(line)
            if numTabs > indention:
                for i in range(numTabs - indention):
                    self.tokenList.append(Token("_INDENT_", lineNum, i + 1, TokenType.INDENT_TOK))
                indention = numTabs
            elif indention > numTabs:
                for i in range(indention - numTabs):
                    self.tokenList.append(Token("_DEDENT_", lineNum, i + 1, TokenType.DEDENT_TOK))
                indention = numTabs
            self.processLine(line, lineNum, numTabs)
        for i in indention:
            self.tokenList.append(Token("_DEDENT_", lineNum, i+1, TokenType.DEDENT_TOK))
        self.tokenList.append(Token("EOS", lineNum + 1, 1, TokenType.EOS_TOK))
        input_file.close()



    def processLine(self, line, lineNum, numTabs):
        assert line is not None and len(line) > 0
        assert lineNum > 0
        assert numTabs >= 0
        index = 0
        index = self.skip_white_space(line, numTabs)
        while index < len(line):
            lexeme = self.get_next_lexeme(line, index)
            tokType = self.get_lexeme_type(lexeme, lineNum, index)
            self.tokenList.append(Token(lexeme, lineNum, index+1, tokType))
            index += len(lexeme)
            index = self.skip_white_space(line, index)
        self.tokenList.append(Token("_EOLN_", lineNum, index + 1, TokenType.EOLN_TOK))


    def get_lexeme_type(self, lexeme, lineNumber, index):
        assert lexeme is not None and len(lexeme) > 0
        assert lineNumber > 0
        assert index >= 0
        type = TokenType.EOS_TOK
        if lexeme[0].isalpha():
            if len(lexeme) == 1:
                type = TokenType.ID_TOK
            elif lexeme == "main":
                type = TokenType.MAIN_TOK
            elif lexeme == "if":
                type = TokenType.IF_TOK
            elif lexeme == "else:":
                type = TokenType.ELSE_TOK
            elif lexeme == "elif":
                type = TokenType.ELIF_TOK
            elif lexeme == "while":
                type = TokenType.WHILE_TOK
            elif lexeme == "print":
                type = TokenType.PRINT_TOK
            else:
                raise LexicalException("reserved word expected at line " + str(lineNumber) + " and column " + str(index + 1))

        elif lexeme[0].isdigit():
            if (Lexical_Analyzer.is_all_digits(self, lexeme)):
                type = TokenType.CONST_TOK
            else:
                raise LexicalException("integer expected at line " + str(lineNumber) + " and column " + str(index + 1))

        elif lexeme == "(":
            type = TokenType.LEFT_PAREN_TOK
        elif lexeme == ")":
            type = TokenType.RIGHT_PAREN_TOK
        elif lexeme == ":":
            type = TokenType.COLON_TOK
        elif lexeme == "==":
            type = TokenType.EQ_TOK
        elif lexeme == "!=":
            type = TokenType.NE_TOK
        elif lexeme == "<":
            type = TokenType.LT_TOK
        elif lexeme == ">":
            type = TokenType.GT_TOK
        elif lexeme == "<=":
            type = TokenType.LE_TOK
        elif lexeme == ">=":
            type = TokenType.GE_TOK
        elif lexeme == "+":
            type = TokenType.ADD_TOK
        elif lexeme == "-":
            type = TokenType.SUB_TOK
        elif lexeme == "/":
            type = TokenType.DIV_TOK
        elif lexeme == "*":
            type = TokenType.MUL_TOK
        elif lexeme == "=":
            type = TokenType.ASSIGN_TOK
        else:
            raise LexicalException("invalid lexeme at line " + str(lineNumber) + " and column " + str(index + 1))
        return type



    def skip_white_space(self, line, index):
        assert line is not None and len(line) > 0
        assert index >= 0
        while (index < len(line) and line[index].isspace()):
            index += 1
        return index

    def find_num_preceding_tabs(self, line):
        assert line is not None and len(line) > 0
        num = 0
        while (num < len(line) and line[num] == '\t'):
            num += 1
        return num

    def get_look_ahead_token(self):
        if not self.tokenList:
            raise RuntimeError("no more tokens")
        return self.tokenList[0]

    def get_next_token(self):
        if not self.tokenList:
            raise RuntimeError("no more tokens")
        return self.tokenList.remove(0)

    def get_next_lexeme(self, line, index):
        assert line is not None and len(line) > 0
        assert index >= 0
        i = index
        while i < len(line) and not line[i].isspace():
            i += 1
        return line[index:i]

    def is_all_digits(self, lexeme):
        assert lexeme is not None and len(lexeme) > 0
        i = 0
        while i < len(lexeme) and lexeme[i].isdigit():
            i += 1
        return i == len(lexeme)