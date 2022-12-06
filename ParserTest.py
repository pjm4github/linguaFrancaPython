import io

from antlr4 import *
from LinguaFrancaLexer import LinguaFrancaLexer
from LinguaFrancaListener import LinguaFrancaListener
from LinguaFrancaParser import LinguaFrancaParser
import sys

class LinguaFrancaPrintListener(LinguaFrancaListener):
    def enterHi(self, ctx):
        print("LinguaFranca: %s" % ctx.ID())

def main():
    mystr = open('./lfSource/Hello.lf', 'r').read()
    instream = InputStream(mystr)

    lexer = LinguaFrancaLexer(instream)
    stream = CommonTokenStream(lexer)
    parser = LinguaFrancaParser(stream)
    tree = parser.model()
    printer = LinguaFrancaPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()