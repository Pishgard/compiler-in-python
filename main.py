from lexer import Lexer
from parsers import Parser

text_input = """
print(20 / 3);
"""

# string = input()

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

pg = Parser()
pg.parse()
parser = pg.get_parser()
parser.parse(tokens).eval()
