#!/usr/bin/env python
""" generated source for module InternalLFLexer """
# package: org.lflang.parser.antlr.internal
#  Hack: Use our own Lexer superclass by means of import. 
#  Currently there is no other way to specify the superclass for the lexer.
# import org.eclipse.xtext.parser.antlr.Lexer

# from org.antlr import runtime
from include.overloading import overloaded
# import java.util.Stack
# import java.util.List
# import java.util.ArrayList
class Lexer:
    pass

@SuppressWarnings("all")
class InternalLFLexer(Lexer):
    """ generated source for class InternalLFLexer """
    EOF = -1
    RULE_ANY_OTHER = 16
    RULE_CHAR_LIT = 10
    RULE_FALSE = 7
    RULE_FLOAT_EXP_SUFFIX = 11
    RULE_ID = 5
    RULE_INT = 8
    RULE_LT_ANNOT = 12
    RULE_ML_COMMENT = 13
    RULE_NEGINT = 9
    RULE_SL_COMMENT = 14
    RULE_STRING = 4
    RULE_TRUE = 6
    RULE_WS = 15
    T__17 = 17
    T__18 = 18
    T__19 = 19
    T__20 = 20
    T__21 = 21
    T__22 = 22
    T__23 = 23
    T__24 = 24
    T__25 = 25
    T__26 = 26
    T__27 = 27
    T__28 = 28
    T__29 = 29
    T__30 = 30
    T__31 = 31
    T__32 = 32
    T__33 = 33
    T__34 = 34
    T__35 = 35
    T__36 = 36
    T__37 = 37
    T__38 = 38
    T__39 = 39
    T__40 = 40
    T__41 = 41
    T__42 = 42
    T__43 = 43
    T__44 = 44
    T__45 = 45
    T__46 = 46
    T__47 = 47
    T__48 = 48
    T__49 = 49
    T__50 = 50
    T__51 = 51
    T__52 = 52
    T__53 = 53
    T__54 = 54
    T__55 = 55
    T__56 = 56
    T__57 = 57
    T__58 = 58
    T__59 = 59
    T__60 = 60
    T__61 = 61
    T__62 = 62
    T__63 = 63
    T__64 = 64
    T__65 = 65
    T__66 = 66
    T__67 = 67
    T__68 = 68
    T__69 = 69
    T__70 = 70
    T__71 = 71
    T__72 = 72
    T__73 = 73
    T__74 = 74
    T__75 = 75
    T__76 = 76
    T__77 = 77
    T__78 = 78
    T__79 = 79
    T__80 = 80
    T__81 = 81
    T__82 = 82
    T__83 = 83
    T__84 = 84
    T__85 = 85

    #  delegates
    #  delegators
    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(InternalLFLexer, self).__init__()

    @__init__.register(object, CharStream)
    def __init___0(self, input):
        """ generated source for method __init___0 """
        super(InternalLFLexer, self).__init__()
        self.__init__(input, RecognizerSharedState())

    @__init__.register(object, CharStream, RecognizerSharedState)
    def __init___1(self, input, state):
        """ generated source for method __init___1 """
        super(InternalLFLexer, self).__init__(state)

    def getGrammarFileName(self):
        """ generated source for method getGrammarFileName """
        return "InternalLF.g"

    #  $ANTLR start "T__17"
    def mT__17(self):
        """ generated source for method mT__17 """
        try:
            _type = self.T__17
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:11:7: ( 'import' )
            #  InternalLF.g:11:9: 'import'
            match("import")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__17"
    #  $ANTLR start "T__18"
    def mT__18(self):
        """ generated source for method mT__18 """
        try:
            _type = self.T__18
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:12:7: ( ',' )
            #  InternalLF.g:12:9: ','
            match(',')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__18"
    #  $ANTLR start "T__19"
    def mT__19(self):
        """ generated source for method mT__19 """
        try:
            _type = self.T__19
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:13:7: ( 'from' )
            #  InternalLF.g:13:9: 'from'
            match("from")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__19"
    #  $ANTLR start "T__20"
    def mT__20(self):
        """ generated source for method mT__20 """
        try:
            _type = self.T__20
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:14:7: ( ';' )
            #  InternalLF.g:14:9: ';'
            match(';')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__20"
    #  $ANTLR start "T__21"
    def mT__21(self):
        """ generated source for method mT__21 """
        try:
            _type = self.T__21
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:15:7: ( 'as' )
            #  InternalLF.g:15:9: 'as'
            match("as")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__21"
    #  $ANTLR start "T__22"
    def mT__22(self):
        """ generated source for method mT__22 """
        try:
            _type = self.T__22
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:16:7: ( 'federated' )
            #  InternalLF.g:16:9: 'federated'
            match("federated")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__22"
    #  $ANTLR start "T__23"
    def mT__23(self):
        """ generated source for method mT__23 """
        try:
            _type = self.T__23
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:17:7: ( 'main' )
            #  InternalLF.g:17:9: 'main'
            match("main")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__23"
    #  $ANTLR start "T__24"
    def mT__24(self):
        """ generated source for method mT__24 """
        try:
            _type = self.T__24
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:18:7: ( 'realtime' )
            #  InternalLF.g:18:9: 'realtime'
            match("realtime")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__24"
    #  $ANTLR start "T__25"
    def mT__25(self):
        """ generated source for method mT__25 """
        try:
            _type = self.T__25
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:19:7: ( 'reactor' )
            #  InternalLF.g:19:9: 'reactor'
            match("reactor")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__25"
    #  $ANTLR start "T__26"
    def mT__26(self):
        """ generated source for method mT__26 """
        try:
            _type = self.T__26
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:20:7: ( '<' )
            #  InternalLF.g:20:9: '<'
            match('<')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__26"
    #  $ANTLR start "T__27"
    def mT__27(self):
        """ generated source for method mT__27 """
        try:
            _type = self.T__27
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:21:7: ( '>' )
            #  InternalLF.g:21:9: '>'
            match('>')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__27"
    #  $ANTLR start "T__28"
    def mT__28(self):
        """ generated source for method mT__28 """
        try:
            _type = self.T__28
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:22:7: ( '(' )
            #  InternalLF.g:22:9: '('
            match('(')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__28"
    #  $ANTLR start "T__29"
    def mT__29(self):
        """ generated source for method mT__29 """
        try:
            _type = self.T__29
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:23:7: ( ')' )
            #  InternalLF.g:23:9: ')'
            match(')')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__29"
    #  $ANTLR start "T__30"
    def mT__30(self):
        """ generated source for method mT__30 """
        try:
            _type = self.T__30
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:24:7: ( 'at' )
            #  InternalLF.g:24:9: 'at'
            match("at")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__30"
    #  $ANTLR start "T__31"
    def mT__31(self):
        """ generated source for method mT__31 """
        try:
            _type = self.T__31
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:25:7: ( 'extends' )
            #  InternalLF.g:25:9: 'extends'
            match("extends")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__31"
    #  $ANTLR start "T__32"
    def mT__32(self):
        """ generated source for method mT__32 """
        try:
            _type = self.T__32
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:26:7: ( '{' )
            #  InternalLF.g:26:9: '{'
            match('{')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__32"
    #  $ANTLR start "T__33"
    def mT__33(self):
        """ generated source for method mT__33 """
        try:
            _type = self.T__33
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:27:7: ( '}' )
            #  InternalLF.g:27:9: '}'
            match('}')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__33"
    #  $ANTLR start "T__34"
    def mT__34(self):
        """ generated source for method mT__34 """
        try:
            _type = self.T__34
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:28:7: ( 'target' )
            #  InternalLF.g:28:9: 'target'
            match("target")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__34"
    #  $ANTLR start "T__35"
    def mT__35(self):
        """ generated source for method mT__35 """
        try:
            _type = self.T__35
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:29:7: ( 'reset' )
            #  InternalLF.g:29:9: 'reset'
            match("reset")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__35"
    #  $ANTLR start "T__36"
    def mT__36(self):
        """ generated source for method mT__36 """
        try:
            _type = self.T__36
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:30:7: ( 'state' )
            #  InternalLF.g:30:9: 'state'
            match("state")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__36"
    #  $ANTLR start "T__37"
    def mT__37(self):
        """ generated source for method mT__37 """
        try:
            _type = self.T__37
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:31:7: ( ':' )
            #  InternalLF.g:31:9: ':'
            match(':')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__37"
    #  $ANTLR start "T__38"
    def mT__38(self):
        """ generated source for method mT__38 """
        try:
            _type = self.T__38
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:32:7: ( 'const' )
            #  InternalLF.g:32:9: 'const'
            match("const")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__38"
    #  $ANTLR start "T__39"
    def mT__39(self):
        """ generated source for method mT__39 """
        try:
            _type = self.T__39
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:33:7: ( 'method' )
            #  InternalLF.g:33:9: 'method'
            match("method")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__39"
    #  $ANTLR start "T__40"
    def mT__40(self):
        """ generated source for method mT__40 """
        try:
            _type = self.T__40
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:34:7: ( 'mutable' )
            #  InternalLF.g:34:9: 'mutable'
            match("mutable")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__40"
    #  $ANTLR start "T__41"
    def mT__41(self):
        """ generated source for method mT__41 """
        try:
            _type = self.T__41
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:35:7: ( 'input' )
            #  InternalLF.g:35:9: 'input'
            match("input")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__41"
    #  $ANTLR start "T__42"
    def mT__42(self):
        """ generated source for method mT__42 """
        try:
            _type = self.T__42
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:36:7: ( 'output' )
            #  InternalLF.g:36:9: 'output'
            match("output")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__42"
    #  $ANTLR start "T__43"
    def mT__43(self):
        """ generated source for method mT__43 """
        try:
            _type = self.T__43
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:37:7: ( 'timer' )
            #  InternalLF.g:37:9: 'timer'
            match("timer")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__43"
    #  $ANTLR start "T__44"
    def mT__44(self):
        """ generated source for method mT__44 """
        try:
            _type = self.T__44
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:38:7: ( 'initial' )
            #  InternalLF.g:38:9: 'initial'
            match("initial")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__44"
    #  $ANTLR start "T__45"
    def mT__45(self):
        """ generated source for method mT__45 """
        try:
            _type = self.T__45
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:39:7: ( 'mode' )
            #  InternalLF.g:39:9: 'mode'
            match("mode")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__45"
    #  $ANTLR start "T__46"
    def mT__46(self):
        """ generated source for method mT__46 """
        try:
            _type = self.T__46
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:40:7: ( 'action' )
            #  InternalLF.g:40:9: 'action'
            match("action")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__46"
    #  $ANTLR start "T__47"
    def mT__47(self):
        """ generated source for method mT__47 """
        try:
            _type = self.T__47
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:41:7: ( 'reaction' )
            #  InternalLF.g:41:9: 'reaction'
            match("reaction")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__47"
    #  $ANTLR start "T__48"
    def mT__48(self):
        """ generated source for method mT__48 """
        try:
            _type = self.T__48
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:42:7: ( 'mutation' )
            #  InternalLF.g:42:9: 'mutation'
            match("mutation")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__48"
    #  $ANTLR start "T__49"
    def mT__49(self):
        """ generated source for method mT__49 """
        try:
            _type = self.T__49
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:43:7: ( '->' )
            #  InternalLF.g:43:9: '->'
            match("->")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__49"
    #  $ANTLR start "T__50"
    def mT__50(self):
        """ generated source for method mT__50 """
        try:
            _type = self.T__50
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:44:7: ( 'deadline' )
            #  InternalLF.g:44:9: 'deadline'
            match("deadline")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__50"
    #  $ANTLR start "T__51"
    def mT__51(self):
        """ generated source for method mT__51 """
        try:
            _type = self.T__51
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:45:7: ( 'STP' )
            #  InternalLF.g:45:9: 'STP'
            match("STP")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__51"
    #  $ANTLR start "T__52"
    def mT__52(self):
        """ generated source for method mT__52 """
        try:
            _type = self.T__52
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:46:7: ( 'preamble' )
            #  InternalLF.g:46:9: 'preamble'
            match("preamble")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__52"
    #  $ANTLR start "T__53"
    def mT__53(self):
        """ generated source for method mT__53 """
        try:
            _type = self.T__53
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:47:7: ( '=' )
            #  InternalLF.g:47:9: '='
            match('=')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__53"
    #  $ANTLR start "T__54"
    def mT__54(self):
        """ generated source for method mT__54 """
        try:
            _type = self.T__54
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:48:7: ( 'new' )
            #  InternalLF.g:48:9: 'new'
            match("new")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__54"
    #  $ANTLR start "T__55"
    def mT__55(self):
        """ generated source for method mT__55 """
        try:
            _type = self.T__55
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:49:7: ( '+' )
            #  InternalLF.g:49:9: '+'
            match('+')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__55"
    #  $ANTLR start "T__56"
    def mT__56(self):
        """ generated source for method mT__56 """
        try:
            _type = self.T__56
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:50:7: ( '~>' )
            #  InternalLF.g:50:9: '~>'
            match("~>")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__56"
    #  $ANTLR start "T__57"
    def mT__57(self):
        """ generated source for method mT__57 """
        try:
            _type = self.T__57
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:51:7: ( 'after' )
            #  InternalLF.g:51:9: 'after'
            match("after")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__57"
    #  $ANTLR start "T__58"
    def mT__58(self):
        """ generated source for method mT__58 """
        try:
            _type = self.T__58
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:52:7: ( 'serializer' )
            #  InternalLF.g:52:9: 'serializer'
            match("serializer")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__58"
    #  $ANTLR start "T__59"
    def mT__59(self):
        """ generated source for method mT__59 """
        try:
            _type = self.T__59
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:53:7: ( '@' )
            #  InternalLF.g:53:9: '@'
            match('@')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__59"
    #  $ANTLR start "T__60"
    def mT__60(self):
        """ generated source for method mT__60 """
        try:
            _type = self.T__60
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:54:7: ( '[' )
            #  InternalLF.g:54:9: '['
            match('[')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__60"
    #  $ANTLR start "T__61"
    def mT__61(self):
        """ generated source for method mT__61 """
        try:
            _type = self.T__61
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:55:7: ( ']' )
            #  InternalLF.g:55:9: ']'
            match(']')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__61"
    #  $ANTLR start "T__62"
    def mT__62(self):
        """ generated source for method mT__62 """
        try:
            _type = self.T__62
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:56:7: ( '.' )
            #  InternalLF.g:56:9: '.'
            match('.')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__62"
    #  $ANTLR start "T__63"
    def mT__63(self):
        """ generated source for method mT__63 """
        try:
            _type = self.T__63
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:57:7: ( 'interleaved' )
            #  InternalLF.g:57:9: 'interleaved'
            match("interleaved")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__63"
    #  $ANTLR start "T__64"
    def mT__64(self):
        """ generated source for method mT__64 """
        try:
            _type = self.T__64
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:58:7: ( 'time' )
            #  InternalLF.g:58:9: 'time'
            match("time")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__64"
    #  $ANTLR start "T__65"
    def mT__65(self):
        """ generated source for method mT__65 """
        try:
            _type = self.T__65
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:59:7: ( '*' )
            #  InternalLF.g:59:9: '*'
            match('*')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__65"
    #  $ANTLR start "T__66"
    def mT__66(self):
        """ generated source for method mT__66 """
        try:
            _type = self.T__66
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:60:7: ( 'widthof(' )
            #  InternalLF.g:60:9: 'widthof('
            match("widthof(")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__66"
    #  $ANTLR start "T__67"
    def mT__67(self):
        """ generated source for method mT__67 """
        try:
            _type = self.T__67
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:61:7: ( '::' )
            #  InternalLF.g:61:9: '::'
            match("::")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__67"
    #  $ANTLR start "T__68"
    def mT__68(self):
        """ generated source for method mT__68 """
        try:
            _type = self.T__68
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:62:7: ( 'physical' )
            #  InternalLF.g:62:9: 'physical'
            match("physical")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__68"
    #  $ANTLR start "T__69"
    def mT__69(self):
        """ generated source for method mT__69 """
        try:
            _type = self.T__69
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:63:7: ( '-' )
            #  InternalLF.g:63:9: '-'
            match('-')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__69"
    #  $ANTLR start "T__70"
    def mT__70(self):
        """ generated source for method mT__70 """
        try:
            _type = self.T__70
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:64:7: ( '%' )
            #  InternalLF.g:64:9: '%'
            match('%')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__70"
    #  $ANTLR start "T__71"
    def mT__71(self):
        """ generated source for method mT__71 """
        try:
            _type = self.T__71
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:65:7: ( '{=' )
            #  InternalLF.g:65:9: '{='
            match("{=")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__71"
    #  $ANTLR start "T__72"
    def mT__72(self):
        """ generated source for method mT__72 """
        try:
            _type = self.T__72
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:66:7: ( '=}' )
            #  InternalLF.g:66:9: '=}'
            match("=}")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__72"
    #  $ANTLR start "T__73"
    def mT__73(self):
        """ generated source for method mT__73 """
        try:
            _type = self.T__73
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:67:7: ( '_' )
            #  InternalLF.g:67:9: '_'
            match('_')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__73"
    #  $ANTLR start "T__74"
    def mT__74(self):
        """ generated source for method mT__74 """
        try:
            _type = self.T__74
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:68:7: ( ':\\\\' )
            #  InternalLF.g:68:9: ':\\\\'
            match(":\\")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__74"
    #  $ANTLR start "T__75"
    def mT__75(self):
        """ generated source for method mT__75 """
        try:
            _type = self.T__75
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:69:7: ( '\\\\' )
            #  InternalLF.g:69:9: '\\\\'
            match('\\')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__75"
    #  $ANTLR start "T__76"
    def mT__76(self):
        """ generated source for method mT__76 """
        try:
            _type = self.T__76
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:70:7: ( '/' )
            #  InternalLF.g:70:9: '/'
            match('/')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__76"
    #  $ANTLR start "T__77"
    def mT__77(self):
        """ generated source for method mT__77 """
        try:
            _type = self.T__77
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:71:7: ( 'startup' )
            #  InternalLF.g:71:9: 'startup'
            match("startup")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__77"
    #  $ANTLR start "T__78"
    def mT__78(self):
        """ generated source for method mT__78 """
        try:
            _type = self.T__78
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:72:7: ( 'shutdown' )
            #  InternalLF.g:72:9: 'shutdown'
            match("shutdown")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__78"
    #  $ANTLR start "T__79"
    def mT__79(self):
        """ generated source for method mT__79 """
        try:
            _type = self.T__79
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:73:7: ( 'widthof' )
            #  InternalLF.g:73:9: 'widthof'
            match("widthof")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__79"
    #  $ANTLR start "T__80"
    def mT__80(self):
        """ generated source for method mT__80 """
        try:
            _type = self.T__80
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:74:7: ( 'history' )
            #  InternalLF.g:74:9: 'history'
            match("history")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__80"
    #  $ANTLR start "T__81"
    def mT__81(self):
        """ generated source for method mT__81 """
        try:
            _type = self.T__81
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:75:7: ( 'logical' )
            #  InternalLF.g:75:9: 'logical'
            match("logical")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__81"
    #  $ANTLR start "T__82"
    def mT__82(self):
        """ generated source for method mT__82 """
        try:
            _type = self.T__82
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:76:7: ( 'private' )
            #  InternalLF.g:76:9: 'private'
            match("private")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__82"
    #  $ANTLR start "T__83"
    def mT__83(self):
        """ generated source for method mT__83 """
        try:
            _type = self.T__83
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:77:7: ( 'public' )
            #  InternalLF.g:77:9: 'public'
            match("public")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__83"
    #  $ANTLR start "T__84"
    def mT__84(self):
        """ generated source for method mT__84 """
        try:
            _type = self.T__84
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:78:7: ( '\\'' )
            #  InternalLF.g:78:9: '\\''
            match('\'')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__84"
    #  $ANTLR start "T__85"
    def mT__85(self):
        """ generated source for method mT__85 """
        try:
            _type = self.T__85
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:79:7: ( 'NONE' )
            #  InternalLF.g:79:9: 'NONE'
            match("NONE")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "T__85"
    #  $ANTLR start "RULE_WS"
    def mRULE_WS(self):
        """ generated source for method mRULE_WS """
        try:
            _type = self.RULE_WS
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:7171:9: ( ( ' ' | '\\t' | '\\r' | '\\n' )+ )
            #  InternalLF.g:7171:11: ( ' ' | '\\t' | '\\r' | '\\n' )+
            #  InternalLF.g:7171:11: ( ' ' | '\\t' | '\\r' | '\\n' )+
            cnt1 = 0
            while True:
                alt1 = 2
                LA1_0 = input.LA(1)
                if ((LA1_0 >= '\t' and LA1_0 <= '\n') or LA1_0 == '\r' or LA1_0 == ' '):
                    alt1 = 1
                if alt1 == 1:
                    #  InternalLF.g:
                    if (input.LA(1) >= '\t' and input.LA(1) <= '\n') or input.LA(1) == '\r' or input.LA(1) == ' ':
                        input.consume()
                    else:
                        mse = MismatchedSetException(None, input)
                        recover(mse)
                        raise mse
                else:
                    if cnt1 >= 1:
                    eee = EarlyExitException(1, input)
                    raise eee
                cnt1 += 1
                if not ((True)):
                    break
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "RULE_WS"
    #  $ANTLR start "RULE_TRUE"
    def mRULE_TRUE(self):
        """ generated source for method mRULE_TRUE """
        try:
            _type = self.RULE_TRUE
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:7173:11: ( ( 'true' | 'True' ) )
            #  InternalLF.g:7173:13: ( 'true' | 'True' )
            #  InternalLF.g:7173:13: ( 'true' | 'True' )
            alt2 = 2
            LA2_0 = input.LA(1)
            if (LA2_0 == 't'):
                alt2 = 1
            elif (LA2_0 == 'T'):
                alt2 = 2
            else:
                nvae = NoViableAltException("", 2, 0, input)
                raise nvae
            if alt2 == 1:
                #  InternalLF.g:7173:14: 'true'
                match("true")
            elif alt2 == 2:
                #  InternalLF.g:7173:21: 'True'
                match("True")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "RULE_TRUE"
    #  $ANTLR start "RULE_FALSE"
    def mRULE_FALSE(self):
        """ generated source for method mRULE_FALSE """
        try:
            _type = self.RULE_FALSE
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:7175:12: ( ( 'false' | 'False' ) )
            #  InternalLF.g:7175:14: ( 'false' | 'False' )
            #  InternalLF.g:7175:14: ( 'false' | 'False' )
            alt3 = 2
            LA3_0 = input.LA(1)
            if (LA3_0 == 'f'):
                alt3 = 1
            elif (LA3_0 == 'F'):
                alt3 = 2
            else:
                nvae = NoViableAltException("", 3, 0, input)
                raise nvae
            if alt3 == 1:
                #  InternalLF.g:7175:15: 'false'
                match("false")
            elif alt3 == 2:
                #  InternalLF.g:7175:23: 'False'
                match("False")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "RULE_FALSE"
    #  $ANTLR start "RULE_ID"
    def mRULE_ID(self):
        """ generated source for method mRULE_ID """
        try:
            _type = self.RULE_ID
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:7177:9: ( ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )* )
            #  InternalLF.g:7177:11: ( 'a' .. 'z' | 'A' .. 'Z' | '_' ) ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )*
            if (input.LA(1) >= 'A' and input.LA(1) <= 'Z') or input.LA(1) == '_' or (input.LA(1) >= 'a' and input.LA(1) <= 'z'):
                input.consume()
            else:
                mse = MismatchedSetException(None, input)
                recover(mse)
                raise mse
            #  InternalLF.g:7177:35: ( 'a' .. 'z' | 'A' .. 'Z' | '_' | '0' .. '9' )*
            while True:
                alt4 = 2
                LA4_0 = input.LA(1)
                if ((LA4_0 >= '0' and LA4_0 <= '9') or (LA4_0 >= 'A' and LA4_0 <= 'Z') or LA4_0 == '_' or (LA4_0 >= 'a' and LA4_0 <= 'z')):
                    alt4 = 1
                if alt4 == 1:
                    #  InternalLF.g:
                    if (input.LA(1) >= '0' and input.LA(1) <= '9') or (input.LA(1) >= 'A' and input.LA(1) <= 'Z') or input.LA(1) == '_' or (input.LA(1) >= 'a' and input.LA(1) <= 'z'):
                        input.consume()
                    else:
                        mse = MismatchedSetException(None, input)
                        recover(mse)
                        raise mse
                else:
                if not ((True)):
                    break
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "RULE_ID"
    #  $ANTLR start "RULE_INT"
    def mRULE_INT(self):
        """ generated source for method mRULE_INT """
        try:
            _type = self.RULE_INT
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:7179:10: ( ( '0' .. '9' )+ )
            #  InternalLF.g:7179:12: ( '0' .. '9' )+
            #  InternalLF.g:7179:12: ( '0' .. '9' )+
            cnt5 = 0
            while True:
                alt5 = 2
                LA5_0 = input.LA(1)
                if ((LA5_0 >= '0' and LA5_0 <= '9')):
                    alt5 = 1
                if alt5 == 1:
                    #  InternalLF.g:7179:13: '0' .. '9'
                    matchRange('0', '9')
                else:
                    if cnt5 >= 1:
                    eee = EarlyExitException(5, input)
                    raise eee
                cnt5 += 1
                if not ((True)):
                    break
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "RULE_INT"
    #  $ANTLR start "RULE_NEGINT"
    def mRULE_NEGINT(self):
        """ generated source for method mRULE_NEGINT """
        try:
            _type = self.RULE_NEGINT
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:7181:13: ( '-' ( '0' .. '9' )+ )
            #  InternalLF.g:7181:15: '-' ( '0' .. '9' )+
            match('-')
            #  InternalLF.g:7181:19: ( '0' .. '9' )+
            cnt6 = 0
            while True:
                alt6 = 2
                LA6_0 = input.LA(1)
                if ((LA6_0 >= '0' and LA6_0 <= '9')):
                    alt6 = 1
                if alt6 == 1:
                    #  InternalLF.g:7181:20: '0' .. '9'
                    matchRange('0', '9')
                else:
                    if cnt6 >= 1:
                    eee = EarlyExitException(6, input)
                    raise eee
                cnt6 += 1
                if not ((True)):
                    break
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "RULE_NEGINT"
    #  $ANTLR start "RULE_FLOAT_EXP_SUFFIX"
    def mRULE_FLOAT_EXP_SUFFIX(self):
        """ generated source for method mRULE_FLOAT_EXP_SUFFIX """
        try:
            _type = self.RULE_FLOAT_EXP_SUFFIX
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:7183:23: ( RULE_INT ( 'e' | 'E' ) ( '+' | '-' )? RULE_INT )
            #  InternalLF.g:7183:25: RULE_INT ( 'e' | 'E' ) ( '+' | '-' )? RULE_INT
            self.mRULE_INT()
            if input.LA(1) == 'E' or input.LA(1) == 'e':
                input.consume()
            else:
                mse = MismatchedSetException(None, input)
                recover(mse)
                raise mse
            #  InternalLF.g:7183:44: ( '+' | '-' )?
            alt7 = 2
            LA7_0 = input.LA(1)
            if (LA7_0 == '+' or LA7_0 == '-'):
                alt7 = 1
            if alt7 == 1:
                #  InternalLF.g:
                if input.LA(1) == '+' or input.LA(1) == '-':
                    input.consume()
                else:
                    mse = MismatchedSetException(None, input)
                    recover(mse)
                    raise mse
            self.mRULE_INT()
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "RULE_FLOAT_EXP_SUFFIX"
    #  $ANTLR start "RULE_SL_COMMENT"
    def mRULE_SL_COMMENT(self):
        """ generated source for method mRULE_SL_COMMENT """
        try:
            _type = self.RULE_SL_COMMENT
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:7185:17: ( ( '//' | '#' ) (~ ( ( '\\n' | '\\r' ) ) )* ( ( '\\r' )? '\\n' )? )
            #  InternalLF.g:7185:19: ( '//' | '#' ) (~ ( ( '\\n' | '\\r' ) ) )* ( ( '\\r' )? '\\n' )?
            #  InternalLF.g:7185:19: ( '//' | '#' )
            alt8 = 2
            LA8_0 = input.LA(1)
            if (LA8_0 == '/'):
                alt8 = 1
            elif (LA8_0 == '#'):
                alt8 = 2
            else:
                nvae = NoViableAltException("", 8, 0, input)
                raise nvae
            if alt8 == 1:
                #  InternalLF.g:7185:20: '//'
                match("//")
            elif alt8 == 2:
                #  InternalLF.g:7185:25: '#'
                match('#')
            #  InternalLF.g:7185:30: (~ ( ( '\\n' | '\\r' ) ) )*
            while True:
                alt9 = 2
                LA9_0 = input.LA(1)
                if ((LA9_0 >= '\u0000' and LA9_0 <= '\t') or (LA9_0 >= '\u000B' and LA9_0 <= '\f') or (LA9_0 >= '\u000E' and LA9_0 <= '\uFFFF')):
                    alt9 = 1
                if alt9 == 1:
                    #  InternalLF.g:7185:30: ~ ( ( '\\n' | '\\r' ) )
                    if (input.LA(1) >= '\u0000' and input.LA(1) <= '\t') or (input.LA(1) >= '\u000B' and input.LA(1) <= '\f') or (input.LA(1) >= '\u000E' and input.LA(1) <= '\uFFFF'):
                        input.consume()
                    else:
                        mse = MismatchedSetException(None, input)
                        recover(mse)
                        raise mse
                else:
                if not ((True)):
                    break
            #  InternalLF.g:7185:46: ( ( '\\r' )? '\\n' )?
            alt11 = 2
            LA11_0 = input.LA(1)
            if (LA11_0 == '\n' or LA11_0 == '\r'):
                alt11 = 1
            if alt11 == 1:
                #  InternalLF.g:7185:47: ( '\\r' )? '\\n'
                #  InternalLF.g:7185:47: ( '\\r' )?
                alt10 = 2
                LA10_0 = input.LA(1)
                if (LA10_0 == '\r'):
                    alt10 = 1
                if alt10 == 1:
                    #  InternalLF.g:7185:47: '\\r'
                    match('\r')
                match('\n')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "RULE_SL_COMMENT"
    #  $ANTLR start "RULE_ML_COMMENT"
    def mRULE_ML_COMMENT(self):
        """ generated source for method mRULE_ML_COMMENT """
        try:
            _type = self.RULE_ML_COMMENT
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:7187:17: ( ( '/*' ( options {greedy=false; } : . )* '*/' | '\\'\\'\\'' ( options {greedy=false; } : . )* '\\'\\'\\'' ) )
            #  InternalLF.g:7187:19: ( '/*' ( options {greedy=false; } : . )* '*/' | '\\'\\'\\'' ( options {greedy=false; } : . )* '\\'\\'\\'' )
            #  InternalLF.g:7187:19: ( '/*' ( options {greedy=false; } : . )* '*/' | '\\'\\'\\'' ( options {greedy=false; } : . )* '\\'\\'\\'' )
            alt14 = 2
            LA14_0 = input.LA(1)
            if (LA14_0 == '/'):
                alt14 = 1
            elif (LA14_0 == '\''):
                alt14 = 2
            else:
                nvae = NoViableAltException("", 14, 0, input)
                raise nvae
            if alt14 == 1:
                #  InternalLF.g:7187:20: '/*' ( options {greedy=false; } : . )* '*/'
                match("/*")
                #  InternalLF.g:7187:25: ( options {greedy=false; } : . )*
                while True:
                    alt12 = 2
                    LA12_0 = input.LA(1)
                    if (LA12_0 == '*'):
                        LA12_1 = input.LA(2)
                        if (LA12_1 == '/'):
                            alt12 = 2
                        elif ((LA12_1 >= '\u0000' and LA12_1 <= '.') or (LA12_1 >= '0' and LA12_1 <= '\uFFFF')):
                            alt12 = 1
                    elif ((LA12_0 >= '\u0000' and LA12_0 <= ')') or (LA12_0 >= '+' and LA12_0 <= '\uFFFF')):
                        alt12 = 1
                    if alt12 == 1:
                        #  InternalLF.g:7187:53: .
                        matchAny()
                    else:
                    if not ((True)):
                        break
                match("*/")
            elif alt14 == 2:
                #  InternalLF.g:7187:62: '\\'\\'\\'' ( options {greedy=false; } : . )* '\\'\\'\\''
                match("'''")
                #  InternalLF.g:7187:71: ( options {greedy=false; } : . )*
                while True:
                    alt13 = 2
                    LA13_0 = input.LA(1)
                    if (LA13_0 == '\''):
                        LA13_1 = input.LA(2)
                        if (LA13_1 == '\''):
                            LA13_3 = input.LA(3)
                            if (LA13_3 == '\''):
                                alt13 = 2
                            elif ((LA13_3 >= '\u0000' and LA13_3 <= '&') or (LA13_3 >= '(' and LA13_3 <= '\uFFFF')):
                                alt13 = 1
                        elif ((LA13_1 >= '\u0000' and LA13_1 <= '&') or (LA13_1 >= '(' and LA13_1 <= '\uFFFF')):
                            alt13 = 1
                    elif ((LA13_0 >= '\u0000' and LA13_0 <= '&') or (LA13_0 >= '(' and LA13_0 <= '\uFFFF')):
                        alt13 = 1
                    if alt13 == 1:
                        #  InternalLF.g:7187:99: .
                        matchAny()
                    else:
                    if not ((True)):
                        break
                match("'''")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "RULE_ML_COMMENT"
    #  $ANTLR start "RULE_LT_ANNOT"
    def mRULE_LT_ANNOT(self):
        """ generated source for method mRULE_LT_ANNOT """
        try:
            _type = self.RULE_LT_ANNOT
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:7189:15: ( '\\'' ( RULE_ID )? )
            #  InternalLF.g:7189:17: '\\'' ( RULE_ID )?
            match('\'')
            #  InternalLF.g:7189:22: ( RULE_ID )?
            alt15 = 2
            LA15_0 = input.LA(1)
            if ((LA15_0 >= 'A' and LA15_0 <= 'Z') or LA15_0 == '_' or (LA15_0 >= 'a' and LA15_0 <= 'z')):
                alt15 = 1
            if alt15 == 1:
                #  InternalLF.g:7189:22: RULE_ID
                self.mRULE_ID()
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "RULE_LT_ANNOT"
    #  $ANTLR start "RULE_STRING"
    def mRULE_STRING(self):
        """ generated source for method mRULE_STRING """
        try:
            _type = self.RULE_STRING
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:7191:13: ( ( '\"' ( '\\\\' . | ~ ( ( '\\\\' | '\"' | '\\t' | '\\r' | '\\n' ) ) )* '\"' | '\"\"\"' ( options {greedy=false; } : . )* '\"\"\"' ) )
            #  InternalLF.g:7191:15: ( '\"' ( '\\\\' . | ~ ( ( '\\\\' | '\"' | '\\t' | '\\r' | '\\n' ) ) )* '\"' | '\"\"\"' ( options {greedy=false; } : . )* '\"\"\"' )
            #  InternalLF.g:7191:15: ( '\"' ( '\\\\' . | ~ ( ( '\\\\' | '\"' | '\\t' | '\\r' | '\\n' ) ) )* '\"' | '\"\"\"' ( options {greedy=false; } : . )* '\"\"\"' )
            alt18 = 2
            LA18_0 = input.LA(1)
            if (LA18_0 == '\"'):
                LA18_1 = input.LA(2)
                if (LA18_1 == '\"'):
                    LA18_2 = input.LA(3)
                    if (LA18_2 == '\"'):
                        alt18 = 2
                    else:
                        alt18 = 1
                elif ((LA18_1 >= '\u0000' and LA18_1 <= '\b') or (LA18_1 >= '\u000B' and LA18_1 <= '\f') or (LA18_1 >= '\u000E' and LA18_1 <= '!') or (LA18_1 >= '#' and LA18_1 <= '\uFFFF')):
                    alt18 = 1
                else:
                    nvae = NoViableAltException("", 18, 1, input)
                    raise nvae
            else:
                nvae = NoViableAltException("", 18, 0, input)
                raise nvae
            if alt18 == 1:
                #  InternalLF.g:7191:16: '\"' ( '\\\\' . | ~ ( ( '\\\\' | '\"' | '\\t' | '\\r' | '\\n' ) ) )* '\"'
                match('\"')
                #  InternalLF.g:7191:20: ( '\\\\' . | ~ ( ( '\\\\' | '\"' | '\\t' | '\\r' | '\\n' ) ) )*
                while True:
                    alt16 = 3
                    LA16_0 = input.LA(1)
                    if (LA16_0 == '\\'):
                        alt16 = 1
                    elif ((LA16_0 >= '\u0000' and LA16_0 <= '\b') or (LA16_0 >= '\u000B' and LA16_0 <= '\f') or (LA16_0 >= '\u000E' and LA16_0 <= '!') or (LA16_0 >= '#' and LA16_0 <= '[') or (LA16_0 >= ']' and LA16_0 <= '\uFFFF')):
                        alt16 = 2
                    if alt16 == 1:
                        #  InternalLF.g:7191:21: '\\\\' .
                        match('\\')
                        matchAny()
                    elif alt16 == 2:
                        #  InternalLF.g:7191:28: ~ ( ( '\\\\' | '\"' | '\\t' | '\\r' | '\\n' ) )
                        if (input.LA(1) >= '\u0000' and input.LA(1) <= '\b') or (input.LA(1) >= '\u000B' and input.LA(1) <= '\f') or (input.LA(1) >= '\u000E' and input.LA(1) <= '!') or (input.LA(1) >= '#' and input.LA(1) <= '[') or (input.LA(1) >= ']' and input.LA(1) <= '\uFFFF'):
                            input.consume()
                        else:
                            mse = MismatchedSetException(None, input)
                            recover(mse)
                            raise mse
                    else:
                    if not ((True)):
                        break
                match('\"')
            elif alt18 == 2:
                #  InternalLF.g:7191:63: '\"\"\"' ( options {greedy=false; } : . )* '\"\"\"'
                match("\"\"\"")
                #  InternalLF.g:7191:69: ( options {greedy=false; } : . )*
                while True:
                    alt17 = 2
                    LA17_0 = input.LA(1)
                    if (LA17_0 == '\"'):
                        LA17_1 = input.LA(2)
                        if (LA17_1 == '\"'):
                            LA17_3 = input.LA(3)
                            if (LA17_3 == '\"'):
                                alt17 = 2
                            elif ((LA17_3 >= '\u0000' and LA17_3 <= '!') or (LA17_3 >= '#' and LA17_3 <= '\uFFFF')):
                                alt17 = 1
                        elif ((LA17_1 >= '\u0000' and LA17_1 <= '!') or (LA17_1 >= '#' and LA17_1 <= '\uFFFF')):
                            alt17 = 1
                    elif ((LA17_0 >= '\u0000' and LA17_0 <= '!') or (LA17_0 >= '#' and LA17_0 <= '\uFFFF')):
                        alt17 = 1
                    if alt17 == 1:
                        #  InternalLF.g:7191:97: .
                        matchAny()
                    else:
                    if not ((True)):
                        break
                match("\"\"\"")
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "RULE_STRING"
    #  $ANTLR start "RULE_CHAR_LIT"
    def mRULE_CHAR_LIT(self):
        """ generated source for method mRULE_CHAR_LIT """
        try:
            _type = self.RULE_CHAR_LIT
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:7193:15: ( '\\'' ( '\\\\' . | ~ ( ( '\\\\' | '\\'' | '\\t' | '\\r' | '\\n' ) ) ) '\\'' )
            #  InternalLF.g:7193:17: '\\'' ( '\\\\' . | ~ ( ( '\\\\' | '\\'' | '\\t' | '\\r' | '\\n' ) ) ) '\\''
            match('\'')
            #  InternalLF.g:7193:22: ( '\\\\' . | ~ ( ( '\\\\' | '\\'' | '\\t' | '\\r' | '\\n' ) ) )
            alt19 = 2
            LA19_0 = input.LA(1)
            if (LA19_0 == '\\'):
                alt19 = 1
            elif ((LA19_0 >= '\u0000' and LA19_0 <= '\b') or (LA19_0 >= '\u000B' and LA19_0 <= '\f') or (LA19_0 >= '\u000E' and LA19_0 <= '&') or (LA19_0 >= '(' and LA19_0 <= '[') or (LA19_0 >= ']' and LA19_0 <= '\uFFFF')):
                alt19 = 2
            else:
                nvae = NoViableAltException("", 19, 0, input)
                raise nvae
            if alt19 == 1:
                #  InternalLF.g:7193:23: '\\\\' .
                match('\\')
                matchAny()
            elif alt19 == 2:
                #  InternalLF.g:7193:30: ~ ( ( '\\\\' | '\\'' | '\\t' | '\\r' | '\\n' ) )
                if (input.LA(1) >= '\u0000' and input.LA(1) <= '\b') or (input.LA(1) >= '\u000B' and input.LA(1) <= '\f') or (input.LA(1) >= '\u000E' and input.LA(1) <= '&') or (input.LA(1) >= '(' and input.LA(1) <= '[') or (input.LA(1) >= ']' and input.LA(1) <= '\uFFFF'):
                    input.consume()
                else:
                    mse = MismatchedSetException(None, input)
                    recover(mse)
                    raise mse
            match('\'')
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "RULE_CHAR_LIT"
    #  $ANTLR start "RULE_ANY_OTHER"
    def mRULE_ANY_OTHER(self):
        """ generated source for method mRULE_ANY_OTHER """
        try:
            _type = self.RULE_ANY_OTHER
            _channel = DEFAULT_TOKEN_CHANNEL
            #  InternalLF.g:7195:16: ( . )
            #  InternalLF.g:7195:18: .
            matchAny()
            state.type = _type
            state.channel = _channel
        finally:

    #  $ANTLR end "RULE_ANY_OTHER"
    def mTokens(self):
        """ generated source for method mTokens """
        #  InternalLF.g:1:8: ( T__17 | T__18 | T__19 | T__20 | T__21 | T__22 | T__23 | T__24 | T__25 | T__26 | T__27 | T__28 | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | T__47 | T__48 | T__49 | T__50 | T__51 | T__52 | T__53 | T__54 | T__55 | T__56 | T__57 | T__58 | T__59 | T__60 | T__61 | T__62 | T__63 | T__64 | T__65 | T__66 | T__67 | T__68 | T__69 | T__70 | T__71 | T__72 | T__73 | T__74 | T__75 | T__76 | T__77 | T__78 | T__79 | T__80 | T__81 | T__82 | T__83 | T__84 | T__85 | RULE_WS | RULE_TRUE | RULE_FALSE | RULE_ID | RULE_INT | RULE_NEGINT | RULE_FLOAT_EXP_SUFFIX | RULE_SL_COMMENT | RULE_ML_COMMENT | RULE_LT_ANNOT | RULE_STRING | RULE_CHAR_LIT | RULE_ANY_OTHER )
        alt20 = 82
        alt20 = dfa20.predict(input)
        if alt20 == 1:
            #  InternalLF.g:1:10: T__17
            self.mT__17()
        elif alt20 == 2:
            #  InternalLF.g:1:16: T__18
            self.mT__18()
        elif alt20 == 3:
            #  InternalLF.g:1:22: T__19
            self.mT__19()
        elif alt20 == 4:
            #  InternalLF.g:1:28: T__20
            self.mT__20()
        elif alt20 == 5:
            #  InternalLF.g:1:34: T__21
            self.mT__21()
        elif alt20 == 6:
            #  InternalLF.g:1:40: T__22
            self.mT__22()
        elif alt20 == 7:
            #  InternalLF.g:1:46: T__23
            self.mT__23()
        elif alt20 == 8:
            #  InternalLF.g:1:52: T__24
            self.mT__24()
        elif alt20 == 9:
            #  InternalLF.g:1:58: T__25
            self.mT__25()
        elif alt20 == 10:
            #  InternalLF.g:1:64: T__26
            self.mT__26()
        elif alt20 == 11:
            #  InternalLF.g:1:70: T__27
            self.mT__27()
        elif alt20 == 12:
            #  InternalLF.g:1:76: T__28
            self.mT__28()
        elif alt20 == 13:
            #  InternalLF.g:1:82: T__29
            self.mT__29()
        elif alt20 == 14:
            #  InternalLF.g:1:88: T__30
            self.mT__30()
        elif alt20 == 15:
            #  InternalLF.g:1:94: T__31
            self.mT__31()
        elif alt20 == 16:
            #  InternalLF.g:1:100: T__32
            self.mT__32()
        elif alt20 == 17:
            #  InternalLF.g:1:106: T__33
            self.mT__33()
        elif alt20 == 18:
            #  InternalLF.g:1:112: T__34
            self.mT__34()
        elif alt20 == 19:
            #  InternalLF.g:1:118: T__35
            self.mT__35()
        elif alt20 == 20:
            #  InternalLF.g:1:124: T__36
            self.mT__36()
        elif alt20 == 21:
            #  InternalLF.g:1:130: T__37
            self.mT__37()
        elif alt20 == 22:
            #  InternalLF.g:1:136: T__38
            self.mT__38()
        elif alt20 == 23:
            #  InternalLF.g:1:142: T__39
            self.mT__39()
        elif alt20 == 24:
            #  InternalLF.g:1:148: T__40
            self.mT__40()
        elif alt20 == 25:
            #  InternalLF.g:1:154: T__41
            self.mT__41()
        elif alt20 == 26:
            #  InternalLF.g:1:160: T__42
            self.mT__42()
        elif alt20 == 27:
            #  InternalLF.g:1:166: T__43
            self.mT__43()
        elif alt20 == 28:
            #  InternalLF.g:1:172: T__44
            self.mT__44()
        elif alt20 == 29:
            #  InternalLF.g:1:178: T__45
            self.mT__45()
        elif alt20 == 30:
            #  InternalLF.g:1:184: T__46
            self.mT__46()
        elif alt20 == 31:
            #  InternalLF.g:1:190: T__47
            self.mT__47()
        elif alt20 == 32:
            #  InternalLF.g:1:196: T__48
            self.mT__48()
        elif alt20 == 33:
            #  InternalLF.g:1:202: T__49
            self.mT__49()
        elif alt20 == 34:
            #  InternalLF.g:1:208: T__50
            self.mT__50()
        elif alt20 == 35:
            #  InternalLF.g:1:214: T__51
            self.mT__51()
        elif alt20 == 36:
            #  InternalLF.g:1:220: T__52
            self.mT__52()
        elif alt20 == 37:
            #  InternalLF.g:1:226: T__53
            self.mT__53()
        elif alt20 == 38:
            #  InternalLF.g:1:232: T__54
            self.mT__54()
        elif alt20 == 39:
            #  InternalLF.g:1:238: T__55
            self.mT__55()
        elif alt20 == 40:
            #  InternalLF.g:1:244: T__56
            self.mT__56()
        elif alt20 == 41:
            #  InternalLF.g:1:250: T__57
            self.mT__57()
        elif alt20 == 42:
            #  InternalLF.g:1:256: T__58
            self.mT__58()
        elif alt20 == 43:
            #  InternalLF.g:1:262: T__59
            self.mT__59()
        elif alt20 == 44:
            #  InternalLF.g:1:268: T__60
            self.mT__60()
        elif alt20 == 45:
            #  InternalLF.g:1:274: T__61
            self.mT__61()
        elif alt20 == 46:
            #  InternalLF.g:1:280: T__62
            self.mT__62()
        elif alt20 == 47:
            #  InternalLF.g:1:286: T__63
            self.mT__63()
        elif alt20 == 48:
            #  InternalLF.g:1:292: T__64
            self.mT__64()
        elif alt20 == 49:
            #  InternalLF.g:1:298: T__65
            self.mT__65()
        elif alt20 == 50:
            #  InternalLF.g:1:304: T__66
            self.mT__66()
        elif alt20 == 51:
            #  InternalLF.g:1:310: T__67
            self.mT__67()
        elif alt20 == 52:
            #  InternalLF.g:1:316: T__68
            self.mT__68()
        elif alt20 == 53:
            #  InternalLF.g:1:322: T__69
            self.mT__69()
        elif alt20 == 54:
            #  InternalLF.g:1:328: T__70
            self.mT__70()
        elif alt20 == 55:
            #  InternalLF.g:1:334: T__71
            self.mT__71()
        elif alt20 == 56:
            #  InternalLF.g:1:340: T__72
            self.mT__72()
        elif alt20 == 57:
            #  InternalLF.g:1:346: T__73
            self.mT__73()
        elif alt20 == 58:
            #  InternalLF.g:1:352: T__74
            self.mT__74()
        elif alt20 == 59:
            #  InternalLF.g:1:358: T__75
            self.mT__75()
        elif alt20 == 60:
            #  InternalLF.g:1:364: T__76
            self.mT__76()
        elif alt20 == 61:
            #  InternalLF.g:1:370: T__77
            self.mT__77()
        elif alt20 == 62:
            #  InternalLF.g:1:376: T__78
            self.mT__78()
        elif alt20 == 63:
            #  InternalLF.g:1:382: T__79
            self.mT__79()
        elif alt20 == 64:
            #  InternalLF.g:1:388: T__80
            self.mT__80()
        elif alt20 == 65:
            #  InternalLF.g:1:394: T__81
            self.mT__81()
        elif alt20 == 66:
            #  InternalLF.g:1:400: T__82
            self.mT__82()
        elif alt20 == 67:
            #  InternalLF.g:1:406: T__83
            self.mT__83()
        elif alt20 == 68:
            #  InternalLF.g:1:412: T__84
            self.mT__84()
        elif alt20 == 69:
            #  InternalLF.g:1:418: T__85
            self.mT__85()
        elif alt20 == 70:
            #  InternalLF.g:1:424: RULE_WS
            self.mRULE_WS()
        elif alt20 == 71:
            #  InternalLF.g:1:432: RULE_TRUE
            self.mRULE_TRUE()
        elif alt20 == 72:
            #  InternalLF.g:1:442: RULE_FALSE
            self.mRULE_FALSE()
        elif alt20 == 73:
            #  InternalLF.g:1:453: RULE_ID
            self.mRULE_ID()
        elif alt20 == 74:
            #  InternalLF.g:1:461: RULE_INT
            self.mRULE_INT()
        elif alt20 == 75:
            #  InternalLF.g:1:470: RULE_NEGINT
            self.mRULE_NEGINT()
        elif alt20 == 76:
            #  InternalLF.g:1:482: RULE_FLOAT_EXP_SUFFIX
            self.mRULE_FLOAT_EXP_SUFFIX()
        elif alt20 == 77:
            #  InternalLF.g:1:504: RULE_SL_COMMENT
            self.mRULE_SL_COMMENT()
        elif alt20 == 78:
            #  InternalLF.g:1:520: RULE_ML_COMMENT
            self.mRULE_ML_COMMENT()
        elif alt20 == 79:
            #  InternalLF.g:1:536: RULE_LT_ANNOT
            self.mRULE_LT_ANNOT()
        elif alt20 == 80:
            #  InternalLF.g:1:550: RULE_STRING
            self.mRULE_STRING()
        elif alt20 == 81:
            #  InternalLF.g:1:562: RULE_CHAR_LIT
            self.mRULE_CHAR_LIT()
        elif alt20 == 82:
            #  InternalLF.g:1:576: RULE_ANY_OTHER
            self.mRULE_ANY_OTHER()

    dfa20 = DFA20(self)
    DFA20_eotS = "\1\uffff\1\64\1\uffff\1\64\1\uffff\3\64\4\uffff\1\64\1\111\1\uffff\2\64\1\123\2\64\1\130\3\64\1\137\1\64\1\uffff\1\61\5\uffff\1\64\1\uffff\1\152\1\uffff\1\156\2\64\1\162\1\64\1\uffff\2\64\1\uffff\1\170\1\uffff\1\61\1\uffff\2\64\2\uffff\3\64\1\uffff\1\u0083\1\u0084\7\64\4\uffff\1\64\3\uffff\6\64\3\uffff\2\64\3\uffff\5\64\2\uffff\1\64\7\uffff\1\64\6\uffff\2\64\1\u00a0\2\uffff\1\64\1\uffff\2\64\1\uffff\1\170\2\uffff\7\64\2\uffff\22\64\1\u00bf\4\64\1\u00c4\3\64\1\uffff\7\64\1\u00cf\4\64\1\u00d4\2\64\1\u00d8\5\64\1\u00df\1\u00e0\7\64\1\uffff\4\64\1\uffff\3\64\1\u00ef\1\u00e0\2\64\1\u00f2\2\64\1\uffff\1\64\1\u00f6\1\64\1\u00f8\1\uffff\3\64\1\uffff\2\64\1\u00ff\2\64\1\u0102\2\uffff\1\u0103\3\64\1\u0107\11\64\1\uffff\1\u00f6\1\u0111\1\uffff\3\64\1\uffff\1\u0115\1\uffff\1\u0116\5\64\1\uffff\1\64\1\u011d\2\uffff\3\64\1\uffff\1\u0121\4\64\1\u0126\3\64\1\uffff\1\u012a\2\64\2\uffff\1\u012d\2\64\1\u0130\1\64\1\u0132\1\uffff\1\u0133\2\64\1\uffff\2\64\1\u0138\1\64\1\uffff\1\u013b\1\u013c\1\u013d\1\uffff\2\64\1\uffff\1\u0140\1\u0141\1\uffff\1\u0142\2\uffff\1\64\1\u0144\1\u0145\1\u0146\1\uffff\1\u0147\4\uffff\1\64\1\u0149\3\uffff\1\64\4\uffff\1\64\1\uffff\1\u014c\1\u014d\2\uffff"
    DFA20_eofS = "\u014e\uffff"
    DFA20_minS = "\1\0\1\155\1\uffff\1\141\1\uffff\1\143\1\141\1\145\4\uffff\1\170\1\75\1\uffff\1\141\1\145\1\72\1\157\1\165\1\60\1\145\1\124\1\150\1\175\1\145\1\uffff\1\76\5\uffff\1\151\1\uffff\1\60\1\uffff\1\52\1\151\1\157\1\0\1\117\1\uffff\1\162\1\141\1\uffff\1\60\1\uffff\1\0\1\uffff\1\160\1\151\2\uffff\1\157\1\144\1\154\1\uffff\2\60\2\164\1\151\2\164\1\144\1\141\4\uffff\1\164\3\uffff\1\162\1\155\1\165\1\141\1\162\1\165\3\uffff\1\156\1\164\3\uffff\1\141\1\120\1\145\1\171\1\142\2\uffff\1\167\7\uffff\1\144\6\uffff\1\163\1\147\1\47\2\uffff\1\116\1\uffff\1\165\1\154\1\uffff\1\60\2\uffff\1\157\1\165\1\164\1\145\1\155\1\145\1\163\2\uffff\1\151\1\145\1\156\1\150\1\141\1\145\1\143\2\145\1\147\2\145\1\162\1\151\1\164\1\163\1\160\1\144\1\60\1\141\1\166\1\163\1\154\1\60\2\164\1\151\1\uffff\1\105\1\145\1\163\1\162\1\164\1\151\1\162\1\60\1\162\1\145\1\157\1\162\1\60\1\157\1\142\1\60\3\164\1\156\1\145\2\60\1\145\1\164\1\141\1\144\1\164\1\165\1\154\1\uffff\1\155\1\141\2\151\1\uffff\1\150\1\157\1\143\2\60\1\145\1\164\1\60\1\141\1\154\1\uffff\1\141\1\60\1\156\1\60\1\uffff\1\144\1\154\1\151\1\uffff\2\151\1\60\1\144\1\164\1\60\2\uffff\1\60\1\165\1\154\1\157\1\60\1\164\1\151\1\142\1\164\2\143\1\157\1\162\1\141\1\uffff\2\60\1\uffff\1\154\1\145\1\164\1\uffff\1\60\1\uffff\1\60\1\145\1\157\1\155\1\162\1\157\1\uffff\1\163\1\60\2\uffff\1\160\1\151\1\167\1\uffff\1\60\1\156\1\154\1\145\1\141\1\60\1\146\1\171\1\154\1\uffff\1\60\1\141\1\145\2\uffff\1\60\1\156\1\145\1\60\1\156\1\60\1\uffff\1\60\1\172\1\156\1\uffff\2\145\1\60\1\154\1\uffff\1\50\2\60\1\uffff\1\166\1\144\1\uffff\2\60\1\uffff\1\60\2\uffff\1\145\3\60\1\uffff\1\60\4\uffff\1\145\1\60\3\uffff\1\162\4\uffff\1\144\1\uffff\2\60\2\uffff"
    DFA20_maxS = "\1\uffff\1\156\1\uffff\1\162\1\uffff\1\164\1\165\1\145\4\uffff\1\170\1\75\1\uffff\1\162\1\164\1\134\1\157\1\165\1\76\1\145\1\124\1\165\1\175\1\145\1\uffff\1\76\5\uffff\1\151\1\uffff\1\172\1\uffff\1\57\1\151\1\157\1\uffff\1\117\1\uffff\1\162\1\141\1\uffff\1\145\1\uffff\1\uffff\1\uffff\1\160\1\164\2\uffff\1\157\1\144\1\154\1\uffff\2\172\2\164\1\151\2\164\1\144\1\163\4\uffff\1\164\3\uffff\1\162\1\155\1\165\1\141\1\162\1\165\3\uffff\1\156\1\164\3\uffff\1\141\1\120\1\151\1\171\1\142\2\uffff\1\167\7\uffff\1\144\6\uffff\1\163\1\147\1\47\2\uffff\1\116\1\uffff\1\165\1\154\1\uffff\1\145\2\uffff\1\157\1\165\1\164\1\145\1\155\1\145\1\163\2\uffff\1\151\1\145\1\156\1\150\1\141\1\145\1\154\2\145\1\147\2\145\1\164\1\151\1\164\1\163\1\160\1\144\1\172\1\141\1\166\1\163\1\154\1\172\2\164\1\151\1\uffff\1\105\1\145\1\163\1\162\1\164\1\151\1\162\1\172\1\162\1\145\1\157\1\162\1\172\1\157\1\164\1\172\3\164\1\156\1\145\2\172\1\145\1\164\1\141\1\144\1\164\1\165\1\154\1\uffff\1\155\1\141\2\151\1\uffff\1\150\1\157\1\143\2\172\1\145\1\164\1\172\1\141\1\154\1\uffff\1\141\1\172\1\156\1\172\1\uffff\1\144\1\154\1\151\1\uffff\1\151\1\157\1\172\1\144\1\164\1\172\2\uffff\1\172\1\165\1\154\1\157\1\172\1\164\1\151\1\142\1\164\2\143\1\157\1\162\1\141\1\uffff\2\172\1\uffff\1\154\1\145\1\164\1\uffff\1\172\1\uffff\1\172\1\145\1\157\1\155\1\162\1\157\1\uffff\1\163\1\172\2\uffff\1\160\1\151\1\167\1\uffff\1\172\1\156\1\154\1\145\1\141\1\172\1\146\1\171\1\154\1\uffff\1\172\1\141\1\145\2\uffff\1\172\1\156\1\145\1\172\1\156\1\172\1\uffff\2\172\1\156\1\uffff\2\145\1\172\1\154\1\uffff\3\172\1\uffff\1\166\1\144\1\uffff\2\172\1\uffff\1\172\2\uffff\1\145\3\172\1\uffff\1\172\4\uffff\1\145\1\172\3\uffff\1\162\4\uffff\1\144\1\uffff\2\172\2\uffff"
    DFA20_acceptS = "\2\uffff\1\2\1\uffff\1\4\3\uffff\1\12\1\13\1\14\1\15\2\uffff\1\21\13\uffff\1\47\1\uffff\1\53\1\54\1\55\1\56\1\61\1\uffff\1\66\1\uffff\1\73\5\uffff\1\106\2\uffff\1\111\1\uffff\1\115\1\uffff\1\122\2\uffff\1\111\1\2\3\uffff\1\4\11\uffff\1\12\1\13\1\14\1\15\1\uffff\1\67\1\20\1\21\6\uffff\1\63\1\72\1\25\2\uffff\1\41\1\113\1\65\5\uffff\1\70\1\45\1\uffff\1\47\1\50\1\53\1\54\1\55\1\56\1\61\1\uffff\1\66\1\71\1\73\1\115\1\116\1\74\3\uffff\1\104\1\121\1\uffff\1\106\2\uffff\1\112\1\uffff\1\114\1\120\7\uffff\1\5\1\16\33\uffff\1\117\36\uffff\1\43\4\uffff\1\46\12\uffff\1\3\4\uffff\1\7\3\uffff\1\35\6\uffff\1\60\1\107\16\uffff\1\105\2\uffff\1\31\3\uffff\1\110\1\uffff\1\51\6\uffff\1\23\2\uffff\1\33\1\24\3\uffff\1\26\11\uffff\1\1\3\uffff\1\36\1\27\6\uffff\1\22\3\uffff\1\32\4\uffff\1\103\3\uffff\1\34\2\uffff\1\30\2\uffff\1\11\1\uffff\1\17\1\75\4\uffff\1\102\1\uffff\1\62\1\77\1\100\1\101\2\uffff\1\40\1\10\1\37\1\uffff\1\76\1\42\1\44\1\64\1\uffff\1\6\2\uffff\1\52\1\57"
    DFA20_specialS = "\1\2\47\uffff\1\1\7\uffff\1\0\u011d\uffff}>"
    DFA20_transitionS = ["\11\61\2\52\2\61\1\52\22\61\1\52\1\61\1\60\1\57\1\61\1\42\1\61\1\50\1\12\1\13\1\40\1\32\1\2\1\24\1\37\1\45\12\56\1\21\1\4\1\10\1\30\1\11\1\61\1\34\5\55\1\54\7\55\1\51\4\55\1\26\1\53\6\55\1\35\1\44\1\36\1\61\1\43\1\61\1\5\1\55\1\22\1\25\1\14\1\3\1\55\1\46\1\1\2\55\1\47\1\6\1\31\1\23\1\27\1\55\1\7\1\20\1\17\2\55\1\41\3\55\1\15\1\61\1\16\1\33\uff81\61", "\1\62\1\63", "", "\1\70\3\uffff\1\67\14\uffff\1\66", "", "\1\74\2\uffff\1\75\14\uffff\1\72\1\73", "\1\76\3\uffff\1\77\11\uffff\1\101\5\uffff\1\100", "\1\102", "", "", "", "", "\1\107", "\1\110", "", "\1\113\7\uffff\1\114\10\uffff\1\115", "\1\117\2\uffff\1\120\13\uffff\1\116", "\1\121\41\uffff\1\122", "\1\124", "\1\125", "\12\127\4\uffff\1\126", "\1\131", "\1\132", "\1\134\11\uffff\1\133\2\uffff\1\135", "\1\136", "\1\140", "", "\1\142", "", "", "", "", "", "\1\150", "", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "", "\1\155\4\uffff\1\154", "\1\157", "\1\160", "\11\163\2\uffff\2\163\1\uffff\31\163\1\155\31\163\32\161\4\163\1\161\1\163\32\161\uff85\163", "\1\164", "", "\1\166", "\1\167", "", "\12\171\13\uffff\1\172\37\uffff\1\172", "", "\11\173\2\uffff\2\173\1\uffff\ufff2\173", "", "\1\174", "\1\176\6\uffff\1\175\3\uffff\1\177", "", "", "\1\u0080", "\1\u0081", "\1\u0082", "", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u0085", "\1\u0086", "\1\u0087", "\1\u0088", "\1\u0089", "\1\u008a", "\1\u008b\21\uffff\1\u008c", "", "", "", "", "\1\u008d", "", "", "", "\1\u008e", "\1\u008f", "\1\u0090", "\1\u0091", "\1\u0092", "\1\u0093", "", "", "", "\1\u0094", "\1\u0095", "", "", "", "\1\u0096", "\1\u0097", "\1\u0098\3\uffff\1\u0099", "\1\u009a", "\1\u009b", "", "", "\1\u009c", "", "", "", "", "", "", "", "\1\u009d", "", "", "", "", "", "", "\1\u009e", "\1\u009f", "\1\163", "", "", "\1\u00a1", "", "\1\u00a2", "\1\u00a3", "", "\12\171\13\uffff\1\172\37\uffff\1\172", "", "", "\1\u00a4", "\1\u00a5", "\1\u00a6", "\1\u00a7", "\1\u00a8", "\1\u00a9", "\1\u00aa", "", "", "\1\u00ab", "\1\u00ac", "\1\u00ad", "\1\u00ae", "\1\u00af", "\1\u00b0", "\1\u00b2\10\uffff\1\u00b1", "\1\u00b3", "\1\u00b4", "\1\u00b5", "\1\u00b6", "\1\u00b7", "\1\u00b9\1\uffff\1\u00b8", "\1\u00ba", "\1\u00bb", "\1\u00bc", "\1\u00bd", "\1\u00be", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u00c0", "\1\u00c1", "\1\u00c2", "\1\u00c3", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u00c5", "\1\u00c6", "\1\u00c7", "", "\1\u00c8", "\1\u00c9", "\1\u00ca", "\1\u00cb", "\1\u00cc", "\1\u00cd", "\1\u00ce", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u00d0", "\1\u00d1", "\1\u00d2", "\1\u00d3", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u00d5", "\1\u00d6\21\uffff\1\u00d7", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u00d9", "\1\u00da", "\1\u00db", "\1\u00dc", "\1\u00dd", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\21\64\1\u00de\10\64", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u00e1", "\1\u00e2", "\1\u00e3", "\1\u00e4", "\1\u00e5", "\1\u00e6", "\1\u00e7", "", "\1\u00e8", "\1\u00e9", "\1\u00ea", "\1\u00eb", "", "\1\u00ec", "\1\u00ed", "\1\u00ee", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u00f0", "\1\u00f1", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u00f3", "\1\u00f4", "", "\1\u00f5", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u00f7", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "", "\1\u00f9", "\1\u00fa", "\1\u00fb", "", "\1\u00fc", "\1\u00fe\5\uffff\1\u00fd", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u0100", "\1\u0101", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "", "", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u0104", "\1\u0105", "\1\u0106", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u0108", "\1\u0109", "\1\u010a", "\1\u010b", "\1\u010c", "\1\u010d", "\1\u010e", "\1\u010f", "\1\u0110", "", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "", "\1\u0112", "\1\u0113", "\1\u0114", "", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u0117", "\1\u0118", "\1\u0119", "\1\u011a", "\1\u011b", "", "\1\u011c", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "", "", "\1\u011e", "\1\u011f", "\1\u0120", "", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u0122", "\1\u0123", "\1\u0124", "\1\u0125", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u0127", "\1\u0128", "\1\u0129", "", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u012b", "\1\u012c", "", "", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u012e", "\1\u012f", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u0131", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u0134", "\1\u0135", "", "\1\u0136", "\1\u0137", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\1\u0139", "", "\1\u013a\7\uffff\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "", "\1\u013e", "\1\u013f", "", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "", "", "\1\u0143", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "", "", "", "", "\1\u0148", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "", "", "", "\1\u014a", "", "", "", "", "\1\u014b", "", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "\12\64\7\uffff\32\64\4\uffff\1\64\1\uffff\32\64", "", ""]
    DFA20_eot = DFA.unpackEncodedString(DFA20_eotS)
    DFA20_eof = DFA.unpackEncodedString(DFA20_eofS)
    DFA20_min = DFA.unpackEncodedStringToUnsignedChars(DFA20_minS)
    DFA20_max = DFA.unpackEncodedStringToUnsignedChars(DFA20_maxS)
    DFA20_accept = DFA.unpackEncodedString(DFA20_acceptS)
    DFA20_special = DFA.unpackEncodedString(DFA20_specialS)
    DFA20_transition = []
    numStates = int()
    i = 0

    class DFA20(DFA):
        """ generated source for class DFA20 """
        def __init__(self, recognizer):
            """ generated source for method __init__ """
            super(DFA20, self).__init__()
            self.recognizer = recognizer
            self.decisionNumber = 20
            self.eot = self.DFA20_eot
            self.eof = self.DFA20_eof
            self.min = self.DFA20_min
            self.max = self.DFA20_max
            self.accept = self.DFA20_accept
            self.special = self.DFA20_special
            self.transition = self.DFA20_transition

        def getDescription(self):
            """ generated source for method getDescription """
            return "1:1: Tokens : ( T__17 | T__18 | T__19 | T__20 | T__21 | T__22 | T__23 | T__24 | T__25 | T__26 | T__27 | T__28 | T__29 | T__30 | T__31 | T__32 | T__33 | T__34 | T__35 | T__36 | T__37 | T__38 | T__39 | T__40 | T__41 | T__42 | T__43 | T__44 | T__45 | T__46 | T__47 | T__48 | T__49 | T__50 | T__51 | T__52 | T__53 | T__54 | T__55 | T__56 | T__57 | T__58 | T__59 | T__60 | T__61 | T__62 | T__63 | T__64 | T__65 | T__66 | T__67 | T__68 | T__69 | T__70 | T__71 | T__72 | T__73 | T__74 | T__75 | T__76 | T__77 | T__78 | T__79 | T__80 | T__81 | T__82 | T__83 | T__84 | T__85 | RULE_WS | RULE_TRUE | RULE_FALSE | RULE_ID | RULE_INT | RULE_NEGINT | RULE_FLOAT_EXP_SUFFIX | RULE_SL_COMMENT | RULE_ML_COMMENT | RULE_LT_ANNOT | RULE_STRING | RULE_CHAR_LIT | RULE_ANY_OTHER );"

        def specialStateTransition(self, s, _input):
            """ generated source for method specialStateTransition """
            input = _input
            _s = s
            if s == 0:
                LA20_48 = input.LA(1)
                s = -1
                if ((LA20_48 >= '\u0000' and LA20_48 <= '\b') or (LA20_48 >= '\u000B' and LA20_48 <= '\f') or (LA20_48 >= '\u000E' and LA20_48 <= '\uFFFF')):
                    s = 123
                else:
                    s = 49
                if s >= 0:
                    return s
            elif s == 1:
                LA20_40 = input.LA(1)
                s = -1
                if (LA20_40 == '\''):
                    s = 109
                elif ((LA20_40 >= 'A' and LA20_40 <= 'Z') or LA20_40 == '_' or (LA20_40 >= 'a' and LA20_40 <= 'z')):
                    s = 113
                elif ((LA20_40 >= '\u0000' and LA20_40 <= '\b') or (LA20_40 >= '\u000B' and LA20_40 <= '\f') or (LA20_40 >= '\u000E' and LA20_40 <= '&') or (LA20_40 >= '(' and LA20_40 <= '@') or (LA20_40 >= '[' and LA20_40 <= '^') or LA20_40 == '`' or (LA20_40 >= '{' and LA20_40 <= '\uFFFF')):
                    s = 115
                else:
                    s = 114
                if s >= 0:
                    return s
            elif s == 2:
                LA20_0 = input.LA(1)
                s = -1
                if (LA20_0 == 'i'):
                    s = 1
                elif (LA20_0 == ','):
                    s = 2
                elif (LA20_0 == 'f'):
                    s = 3
                elif (LA20_0 == ';'):
                    s = 4
                elif (LA20_0 == 'a'):
                    s = 5
                elif (LA20_0 == 'm'):
                    s = 6
                elif (LA20_0 == 'r'):
                    s = 7
                elif (LA20_0 == '<'):
                    s = 8
                elif (LA20_0 == '>'):
                    s = 9
                elif (LA20_0 == '('):
                    s = 10
                elif (LA20_0 == ')'):
                    s = 11
                elif (LA20_0 == 'e'):
                    s = 12
                elif (LA20_0 == '{'):
                    s = 13
                elif (LA20_0 == '}'):
                    s = 14
                elif (LA20_0 == 't'):
                    s = 15
                elif (LA20_0 == 's'):
                    s = 16
                elif (LA20_0 == ':'):
                    s = 17
                elif (LA20_0 == 'c'):
                    s = 18
                elif (LA20_0 == 'o'):
                    s = 19
                elif (LA20_0 == '-'):
                    s = 20
                elif (LA20_0 == 'd'):
                    s = 21
                elif (LA20_0 == 'S'):
                    s = 22
                elif (LA20_0 == 'p'):
                    s = 23
                elif (LA20_0 == '='):
                    s = 24
                elif (LA20_0 == 'n'):
                    s = 25
                elif (LA20_0 == '+'):
                    s = 26
                elif (LA20_0 == '~'):
                    s = 27
                elif (LA20_0 == '@'):
                    s = 28
                elif (LA20_0 == '['):
                    s = 29
                elif (LA20_0 == ']'):
                    s = 30
                elif (LA20_0 == '.'):
                    s = 31
                elif (LA20_0 == '*'):
                    s = 32
                elif (LA20_0 == 'w'):
                    s = 33
                elif (LA20_0 == '%'):
                    s = 34
                elif (LA20_0 == '_'):
                    s = 35
                elif (LA20_0 == '\\'):
                    s = 36
                elif (LA20_0 == '/'):
                    s = 37
                elif (LA20_0 == 'h'):
                    s = 38
                elif (LA20_0 == 'l'):
                    s = 39
                elif (LA20_0 == '\''):
                    s = 40
                elif (LA20_0 == 'N'):
                    s = 41
                elif ((LA20_0 >= '\t' and LA20_0 <= '\n') or LA20_0 == '\r' or LA20_0 == ' '):
                    s = 42
                elif (LA20_0 == 'T'):
                    s = 43
                elif (LA20_0 == 'F'):
                    s = 44
                elif ((LA20_0 >= 'A' and LA20_0 <= 'E') or (LA20_0 >= 'G' and LA20_0 <= 'M') or (LA20_0 >= 'O' and LA20_0 <= 'R') or (LA20_0 >= 'U' and LA20_0 <= 'Z') or LA20_0 == 'b' or LA20_0 == 'g' or (LA20_0 >= 'j' and LA20_0 <= 'k') or LA20_0 == 'q' or (LA20_0 >= 'u' and LA20_0 <= 'v') or (LA20_0 >= 'x' and LA20_0 <= 'z')):
                    s = 45
                elif ((LA20_0 >= '0' and LA20_0 <= '9')):
                    s = 46
                elif (LA20_0 == '#'):
                    s = 47
                elif (LA20_0 == '\"'):
                    s = 48
                elif ((LA20_0 >= '\u0000' and LA20_0 <= '\b') or (LA20_0 >= '\u000B' and LA20_0 <= '\f') or (LA20_0 >= '\u000E' and LA20_0 <= '\u001F') or LA20_0 == '!' or LA20_0 == '$' or LA20_0 == '&' or LA20_0 == '?' or LA20_0 == '^' or LA20_0 == '`' or LA20_0 == '|' or (LA20_0 >= '\u007F' and LA20_0 <= '\uFFFF')):
                    s = 49
                if s >= 0:
                    return s
            nvae = NoViableAltException(self.getDescription(), 20, _s, input)
            error(nvae)
            raise nvae
