__author__ = 'Chris'

import sys
from Parser_Exception import ParserException
from Lexical_Exception import LexicalException
from Parser import Parser

class Interpreter:
    def main(self):
        try:
            p = Parser("test1.py")
            prog = p.parse()
            prog.execute()
        except FileNotFoundError:
            print("source file not found")
        except LexicalException as e:
            print(e)
        except ParserException as e:
            print(e)
        except:
            print("unknown error occurred - ending process", sys.exc_info())
            raise

    if __name__ == '__main__':
        main()

