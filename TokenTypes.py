__author__ = 'Chris'


class TokenType:
    MAIN_TOK, LEFT_PAREN_TOK, RIGHT_PAREN_TOK, EOLN_TOK, INDENT_TOK, DEDENT_TOK, IF_TOK, COLON_TOK, ELSE_TOK, ELIF_TOK, WHILE_TOK, ID_TOK, PRINT_TOK, CONST_TOK, GE_TOK, GT_TOK, LE_TOK, LT_TOK, EQ_TOK, NE_TOK, ADD_TOK, SUB_TOK, MUL_TOK, DIV_TOK, ASSIGN_TOK, EOS_TOK = range(26)