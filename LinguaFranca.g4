/* The Lingua Franca grammar. */
// from https://github.com/lf-lang/lingua-franca/blob/master/org.lflang/src/org/lflang/LinguaFranca.xtext
/*************
Copyright (c) 2020, The University of California at Berkeley.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES 
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; 
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON 
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT 
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS 
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
***************/

/** 
 * Grammar for Lingua Franca.
 * A note of caution: extending this grammar with productions that introduce
 * new terminals (i.e., anything written between quotes), will require those 
 * terminals to also be added to the Token production at the bottom of this
 * file. Failing to do so will cause a parse error whenever a terminal not
 * listed in the Token production is featured in a segment of target-language
 * code (e.g., a reaction body).
 * @author{Marten Lohstroh <marten@berkeley.edu>}
 * @author{Edward A. Lee <eal@berkeley.edu>}
 */

grammar LinguaFranca;  //org.lflang.LF
   // hidden(WS, ML_COMMENT, SL_COMMENT)

//import "http://www.eclipse.org/emf/2002/Ecore" as ecore

// Use the package name "lf" for generated files defining the classes
// in the metamodel (i.e., the classes representing nodes in the
// abstract syntax tree (AST), i.e., the eCore model). 
//generate lf "https://lf-lang.org"

/////////// Overall file

/**
 * Top-level AST node.
 */

model: targetDecl
    importDecl*
    preamble*
    reactor+
    ;

/**
 * Specification of the target language. Target properties can be specified in
 * YAML format to pass on configuration details to the runtime environment.
 */

targetDecl: 'target' ID keyValuePairs? ';'? ;

/////////// Top level elements

/**
 * importDecl declaration.
 */
importDecl: 'import' importedReactor+ (COMMA importedReactor+)* 'from' STRING ';'?;

reactorDecl: (reactor | importedReactor);

//importedReactor: reactor ('as' ID)?;
importedReactor: ID ('as' ID)?;


/**
 * Declaration of a reactor class.
 */
reactor:  attribute* ('federated' | 'main')? 'realtime'? 'reactor' ID?
    ('<' typeParm (COMMA typeParm)* '>')?
    argumentsForm3?
    ('at' host)?
    ('extends' (reactorDecl (COMMA reactorDecl)*))?
    '{'
    (preamble
        | stateVar
        | method
        | inputDecl
        | outputDecl
        | timer
        | action
        | instantiation
        | connection
        | reaction
        | modeDecl
    )* '}'
    ;

typeParm:
    typeExpr | code
    ;

// Allows simple statements like "A extends B". We probably want to further expand this.
typeExpr:
    ID+
    ;

/////////// Statements

/**
 * Declaration of a state variable. Types are optional, but may be required 
 * during validation (depending on the target language). Initialization is also 
 * optional. A state variable can be initialized by assigning a `Expression` or list
 * of these. Note that a `Expression` may also be a reference to a parameter.
 * The following checks must be carried out during validation: 
 *  - if the list of initialization expressions has more than one element in it, a
 *  type must be specified;
 *  - if the `time` type is specified, there can only be a single initialization
 *  element, which has to denote a time or a reference to a parameter that
 *  denotes a time; and
 *  - if the `time` type is specified, either a proper time interval and unit
 *  must be given, or a literal or code that denotes zero.
 */
stateVar:
    attribute*
    ('reset')? 'state' ID (':' type)?
   argumentsForm1?
    //    ('(' INT* (COMMA  INT)* ')')?
 //       ('{' Literal* (COMMA  Literal*)* '}')?
    argumentsForm2?
//        ('{' INT* (COMMA  INT*)* '}')?
    ';'?
    ;

method:
    'const'? 'method' ID
    '(' (methodArgument (COMMA methodArgument)*)? ')'
    (':' type)?
    code
    ';'?
    ;

methodArgument:
    ID (':' type)?
    ;

inputDecl:
    attribute* 'mutable'? 'input' (widthSpec)? ID (':' type)? ';'?;

outputDecl:
    attribute* 'output' (widthSpec)? ID (':' type)? ';'?;

// Timing specification for a timer: (offset, period)
// Can be empty, which means (0,0) = (NOW, ONCE).
// E.g. (0) or (NOW) or (NOW, ONCE) or (100, 1000)
// The latter means fire with period 1000, offset 100.
timer:
   attribute* 'timer' ID ('(' expression (COMMA expression)? ')')? ';'?;

modeDecl: ('initial')? 'mode' ID?
        '{' ( stateVar
           | timer
           | action
           | instantiation
           | connection
           | reaction)*
        '}'
        ;

// Action that has either a physical or logical origin.
// 
// If the origin is logical, the minDelay is a minimum logical delay
// after the logical time at which schedule() is called that the
// action will occur. If the origin is physical, then the 
// minDelay is a minimum logical delay after the physical time
// at which schedule() is called that the action will occur.
//
// For all actions, minSpacing is the minimum difference between
// the tags of two subsequently scheduled events.
action:
    attribute*
    actionOrigin? 'action' ID
    argumentsForm1?
//    ('(' expression (COMMA? expression )? ')')
    (':' type)? ';'?
    ;

reaction:
    attribute*
    ('reaction' | 'mutation')
    ('(' (triggerRef (COMMA triggerRef)*)? ')')?
    (varRef (COMMA varRef)*)?
    ('->' varRefOrModeTransition (COMMA varRefOrModeTransition)*)?
    code
    sTP?
    deadline?
    ;

triggerRef:
    builtinTriggerRef | varRef;

builtinTriggerRef:
    builtinTrigger;

deadline:
    'deadline' '(' expression ')' code;
    
sTP:
    'STP' '(' expression ')' code;

preamble:
    visibility? 'preamble' code;

instantiation:
    ID '=' 'new' widthSpec? ID
    ('<' typeParm (COMMA typeParm)* '>')?
    '(' ( assignment (COMMA assignment)*)? ')'
    (('at' host ';') | ';')?
    ;

connection:
    ( ( varRef (COMMA varRef)*)
      | ( '(' varRef (COMMA varRef)* ')' '+'?)
    )
    ('->' | '~>')
    varRef (COMMA varRef)*
    ('after' expression)?
    serializer?
    ';'?
    ;

// Chooses the serializer to use for the connection
serializer:
    'serializer' STRING
    ;

/////////// Attributes
attribute:
    '@' ID ('(' ( attrParm (COMMA attrParm)* COMMA?)? ')')?
    ;

attrParm:
    (ID '=')? attrParmValue;

attrParmValue:
      STRING
    | INT
    | NEGINT
    | Boolean
    | SignedFloat
    ;

// For target parameters

keyValuePairs:
    '{' ( keyValuePair ((COMMA| TimeUnit) ( keyValuePair))*)? '}';

//keyValuePair: Kebab ':' element;
keyValuePair: ID ':' (value | valueArray)
    ;

array: // todo allow empty array in grammar, replace with validator error
    '[' element (COMMA ( element))* COMMA? ']'
    ;

element:
        value
    | INT
    | NEGINT
    | Boolean
    | SignedFloat
    | Path
    | array
    | STRING
    ;

// Pieces
typedVariable:
    portDecl | action
    ;

variable:
    typedVariable | timer | modeDecl
    ;

varRef: ID
    | variable
    | DottedName
    | instantiation '.' variable
    | ('interleaved'
        '('
            (variable | instantiation '.' variable)
        ')'
    )
    ;

varRefOrModeTransition:
    varRef | modeTransition '(' modeDecl ')'
    ;

assignment:
    parameter (
        ('=' expression)
        | ('='? (argumentsForm1 | argumentsForm2))
    )
    ;

/**
 * Parameter declaration with optional type and mandatory initialization.
 */
parameter:
    attribute* ID (':' type)?
    ( argumentsForm1
    | argumentsForm2
    )?
    ;

argumentsForm1:
    '(' ( expression (COMMA expression)*)? ')';
argumentsForm2:
    '{' ( expression (COMMA expression)*)? '}';
argumentsForm3:
    '(' parameter (COMMA parameter)* ')';
argumentsForm4:
    '(' (parameter (COMMA parameter)*)? ')';

expression:
    // Literal
    parameter
    | value
    | code
    ;

value: ((SignedFloat | INT | NEGINT) (TimeUnit)?)
        | STRING
        | Boolean
        ;

valueArray:
    '[' value (COMMA value)* ']'
    ;

//parameterReference: parameter;

portDecl:
    inputDecl | outputDecl;
    
// A type is in the target language, hence either an ID or target code.
type:
    'time' arraySpec?
    | DottedName ('<' type (COMMA type)* '>')? ('*')* arraySpec?
    | code
    ;

arraySpec:
    OPEN_CLOSE_SQ_BR | '[' INT ']';
    
widthSpec:
    OPEN_CLOSE_SQ_BR | '[' widthTerm ('+' widthTerm)* ']';
    
widthTerm: INT
    | parameter
    | 'widthof(' varRef ')'
    | code
    ;

ipV4host:
    (Kebab '@')? IPV4Addr (':' INT)?
    ;

ipV6host:
    ('[' (Kebab '@')? IPV6Addr ']' (':' INT)?)
    ;

namedHost:
    (Kebab '@')? hostName (':' INT)?
    ;

host:
    ipV4host | ipV6host | namedHost
    ;

hostName:
    Kebab ('.' Kebab)*
    ;

// FIXME: What if the code needs to contain '=}'?
// Just escaping with \ is not a good idea because then every \ has to be escaped \\.
// Perhaps the string EQUALS_BRACE could become '=}'?
code:
    //{Code} '{=' ( Token)* '=}'
    SC_MARK (~EC_MARK)* EC_MARK
    ;

// Enums
actionOrigin:
    'logical' | 'physical';

visibility:
    'private' | 'public';

builtinTrigger: 'startup' | 'shutdown'  | 'reset';

modeTransition: 'reset' | 'history';

COMMA:
    ','
    ;

Boolean:
    TRUE | FALSE
    ;

//TIME:
//    INT TimeUnit
//    ;

DottedName:
    ID ('.'|'::') ID+
    ;

//SignedInt:
//    INT | NEGINT
//;

//Literal:
//    STRING | CHAR_LIT | SignedFloat | INT | NEGINT | Boolean
//    ;

/////////// Elementary components

/////////// Lexical grammar
// Terminals must be mutually exclusive. They are used by the lexer before parsing.

// Note that the rest of the grammar implicitly defines
// keywords for every string literal, eg 'reaction'.

WS: (' '|'\t'|'\n'|'\r')+ -> channel(HIDDEN)
    ;

// PERFORMANCE: 'fast' | 'timeout';

TRUE:  'true' | 'True';
FALSE: 'false' | 'False';
ID: [a-zA-Z_] [a-zA-Z0-9_]* ; // match usual identifier spec
INT: [0-9]+;
NEGINT: '-' INT;

FLOAT_EXP_SUFFIX: INT ('e' | 'E') ('+' | '-')? INT;

SL_COMMENT: ('//' | '#')  ~('\n'|'\r')* ('\r'? '\n')? -> skip;

ML_COMMENT:  '/*' .*? '*/' WS? -> skip;

LT_ANNOT: '\'' ID?;

STRING:
    '"' ( '\\' . | ~('\\' | '"' | '\t' | '\r' | '\n') )* '"'
    | '"""'
    ;

CHAR_LIT: '\'' ( '\\' . | ~('\\' | '\'' | '\t' | '\r' | '\n') )  '\'';

ANY_OTHER: .;


Kebab: (ID|'physical')('-'ID)*;

IPV4Addr:
    INT '.' INT '.' INT '.' INT
    ;

HEXDIG:
   [0-9] | [A-F] | [a-f];

H16:
    HEXDIG HEXDIG HEXDIG HEXDIG
    | HEXDIG HEXDIG HEXDIG
    | HEXDIG HEXDIG
    | HEXDIG
    ;

LS32:
    H16 ':' H16
    | IPV4Addr
    ;

IPV6Addr:
    H16 ':' H16 ':' H16 ':' H16 ':' H16 ':' H16 ':' LS32
    | '::' H16 ':' H16 ':' H16 ':' H16 ':' H16 ':' LS32
    | H16? '::' H16 ':' H16 ':' H16 ':' H16 ':' LS32
    | ((H16 ':')? H16)? '::' H16 ':' H16 ':' H16 ':' LS32
    | (((H16 ':')? H16 ':')? H16)? '::' H16 ':' H16 ':' LS32
    | ((((H16 ':')? H16 ':')? H16 ':')? H16)? '::' H16 ':' LS32
    | (((((H16 ':')? H16 ':')? H16 ':')? H16 ':')? H16)? '::' LS32
    | ((((((H16 ':')? H16 ':')? H16 ':')? H16 ':')? H16 ':')? H16)? '::' H16
    ;

//
//IPV6Seg:
//    // NOTE: This rule is too permissive by design.
//    // Further checking is done during validation.
//    INT | (INT? ID)
//;
//
//
//IPV6Addr:
//    // NOTE: This rule is too permissive by design.
//    // Further checking is done during validation.
//    // IPV6 with truncation.
//    '::' | ('::' (IPV6Seg (':'))* IPV6Seg) | ((IPV6Seg (':'|'::'))+ IPV6Seg?) |
//
//    // (Link-local IPv6 addresses with zone index) "fe80::7:8%1"
//    (ID '::' IPV6Seg (':' IPV6Seg)* '%' (INT | ID)+) |
//
//    // IPv4-mapped IPv6 addresses and IPv4-translated addresses
//    ('::' IPV4Addr) | ('::' ID ':' (INT ':')? IPV4Addr) |
//
//    // IPv4-Embedded IPv6 Address
//    (((IPV6Seg (':' IPV6Seg)* '::') | (IPV6Seg (':' IPV6Seg)*) ':') IPV4Addr)
//;


SignedFloat:
    (INT | NEGINT | '-')? '.' (INT | FLOAT_EXP_SUFFIX);

FileName:
    (ID | '.' | '_')+
    ;
// Absolute or relative directory path in Windows, Linux, or MacOS.
Path:
    (FileName ':\\')? ('\\' | '/')? FileName (('\\' | '/') FileName)*
    ;

// Note: time units are not keywords, otherwise it would reserve
// a lot of useful identifiers (like 's' or 'd').
// The validator ensures the unit is valid.
//TimeUnit: ID;
// Check Gain.lf and DoubleInvocation.lf
// https://stackoverflow.com/questions/24194110/antlr4-negative-lookahead-in-lexer
TimeUnit: WS+  // Whitespace is needed here to grab the timeunit
    (((('n' | 'u' | 'm')? ('sec' | 'second'))
    | 'minute' | 'min'
    | 'hour' | 'day' | 'week') ('s')?)
    (WS+ | {return ',' if self._input.LA(1) == ',' else None}) // Whitespace is needed here to ensure this is a word
    ;

// An arbitrary sequence of terminals.
//Body:
//    Token+
//;
// KEYWORDS, TOKENS

OPEN_CLOSE_SQ_BR: '[]';
// Production for the tokenization of target code. All terminals used in any
// of the productions in the grammar (except for `{=` and `=}`) have to be
// listed here. Whenever a terminal is encountered amid a sequence of target-
// language tokens that is not featured in this production, this will demarcate
// the end of a target-code segment.

// Start code mark
SC_MARK: '{=';
// End code mark
EC_MARK: '=}';

Token:
    // Non-constant terminals
    FLOAT_EXP_SUFFIX | LT_ANNOT | STRING | CHAR_LIT | ML_COMMENT | SL_COMMENT |  ANY_OTHER |
    //WS |
    // Keywords
    'target' |
    'import' | 'main' | 'realtime' | 'reactor' | 'state' | 'time' |
    'mutable' | 'input' | 'output' | 'timer' | 'action' | 'reaction' |
    'startup' | 'shutdown' |
    'after' | 'deadline' | 'mutation' | 'preamble' |
    'new' | 'federated' | 'at' | 'as' | 'from' | 'widthof' | 'const' | 'method' |
    'interleaved' | 'mode' | 'initial' |
     'reset' | 'history' |
    // Other terminals
    NEGINT |
    // Action origins
    'logical' | 'physical' |
    // Visibility modifiers
    'private' | 'public' |
    // Braces
    '(' | ')' | '{' | '}' |
    // Brackets
    '[' | ']' | '<' | '>' |
    // Punctuation
    ':' | ';' | COMMA | '.' |
    // Slashes
    ':\\' | '\\' |
    // Arithmetic
    '+' | '-' | '*' | '/' |
    // Underscore
    '_' |
    // Arrow
    '->' | 
    // Assignment
    '=' |
    // Percentage
    '%' |
    // Annotation
    '@' |
    // Single quotes
    '\'' |
    // Hash
    '#'
    ;

