"""Lexer for (Standardized) Pseudocode in Pygments."""
import re

from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import Punctuation, Text, Comment, \
    Operator, Keyword, Name, String, Number

class PseudocodeLexer(RegexLexer):
    """Lex our Pseudocode According to the Standard."""
    # Comments
    # -----------------------------------------------------------------------
    ## C Style Block
    myComments = '\/\*.*\*\/|'
    ## C/Sh Style Line
    myComments += '\/\/.*\n|#.*\n|'
    ## Lisp Style Line
    myComments += ';.*\n'
    # -----------------------------------------------------------------------

    # Keywords
    # -----------------------------------------------------------------------
    ## Input
    myKeywords = 'read|obtain|get|from|take|use|copy|'
    ## Output
    myKeywords += 'print|display|show|save|return|'
    ## Compute
    myKeywords += 'compute|calculate|determine|append|to|'
    ## Initialize
    myKeywords += 'set|initialize|init|let|is|has|'
    ## Add/Sub one
    myKeywords += 'increment|bump|decrement|'
    ## If-Then-Else
    myKeywords += 'if|then|else|otherwise|when|unless|'
    ## (Do) While
    myKeywords += 'while|done|endwhile|do|'
    ## Case
    myKeywords += 'case|of|others|endcase|'
    ## Repeat Until
    myKeywords += 'repeat|until|'
    ## For
    myKeywords += 'for|endfor|'
    ## Program Flow
    myKeywords += 'call|exception|as|recurse|begin|end|'
    ## Abstractions
    myKeywords += 'this|that|except|in|'
    ## Type Ops
    myKeywords += 'convert|cast|ensure|expecting|expect'
    # -----------------------------------------------------------------------

    # Constants
    # -----------------------------------------------------------------------
    ## Booleans
    myConstants = 'true|false|'
    ## Unbound
    myConstants += 'nonexistant|unbound|missing|null|'
    ## Status
    myConstants += 'success|failure|'
    ## Formatting
    myConstants += 'newline|beep|indent|'
    ## Assumptions
    myConstants += 'user|screen|system'
    # -----------------------------------------------------------------------

    # Datatypes
    # -----------------------------------------------------------------------
    ## Basics
    myDatatypes = 'number|string|character|boolean|'
    ## Extended Boolean
    myDatatypes += 'truthy|falsey|'
    ## Collections
    myDatatypes += 'list|array|sequence|every|each|'
    ## Abstractions
    myDatatypes += 'nothing|maybe|symbol|many|any|'
    ## Program
    myDatatypes += 'constant|operator|procedure|'
    ## OS
    myDatatypes += 'file|stream|pipe|port|line|interrupt|'
    ## Results
    myDatatypes += 'sum|difference|product|quotient|remainder|'
    ## References
    myDatatypes += 'value|name|result|message|field|a'
    # -----------------------------------------------------------------------

    # Operator Symbols
    # -----------------------------------------------------------------------
    ## Comparison
    myOperators =  '>\s|<\s|==|!=|<>|<=|>=|=|!<|!>|≡|≯|≮|≥|≤|≠|'
    ## Logical
    myOperators += '¬|⊻|∨|∧|&&|\|\||'
    ## Arrows
    myOperators += '->|<-|→|←|'
    ## Arithmetic
    myOperators += '\^|\*|\+|-|\/|\%|×|÷'
    # -----------------------------------------------------------------------

    # Operator Words
    # -----------------------------------------------------------------------
    ## Comparison Words 1
    myOperatorWords = 'less than|more than|greater than|'
    ## Comparison Words 2
    myOperatorWords += 'equal to|different than|different from|'
    ## Logical Words
    myOperatorWords += 'not|xor|and|or|exclusive|'
    ## Arrows Words
    myOperatorWords += 'resulting in|fed|right|left'
    ## Arithmetic Words 1
    myOperatorWords += 'plus|minus|times|divided by|modulo|'
    ## Arithmetic Words 2
    myOperatorWords += 'add|subtract|multiply|divide|'
    ## Artihmetic Words 3
    myOperatorWords += 'take the remainder of|raised to|'
    ## Arithmetic Words 4
    myOperatorWords += 'power|squared|cubed|root|square|cube'
    # -----------------------------------------------------------------------

    # Misc
    # -----------------------------------------------------------------------
    ## Basics
    myPunctuation = '[(),:.?] '
    ## Brackets
    myFunctions = '\[.*\S+.*\]\s'
    ## Capital Initial
    myVariables = '[A-Z]\w*'
    ## Scientific Notation
    myComplexNumbers = '`.*\S.*`'
    ## End of Token Indicators
    endOfToken = '(?= |\.|\n|:|,)'
    # -----------------------------------------------------------------------

    # Metadata
    # -----------------------------------------------------------------------
    name = 'Pseudocode (std)'
    aliases = ['pseudocode', 'pseudo', 'algorithm', 'algo']
    filenames = ['*.algo', '*.pseudocode']
    mimetypes = []
    # -----------------------------------------------------------------------

    # Helper Functions
    # -----------------------------------------------------------------------
    ## Operator Replace
    def op_replace(lexer, match):
        """Replace ASCII operators with Unicode equivalents."""
        op = match.group(0)

        S = ('<=', '>=', '<>', '!=', '==', '->', '<-', '*', '/', '!<', '!>',
             '||', '&&')
        R = ('≤', '≥', '≠', '≠', '≡', '→', '←', '×', '÷', '≮', '≯', '∨', '∧')

        if op in S:
            op = R[S.index(op)]

        yield match.start(), Operator, op
    ## Number Replace
    def num_replace(lexer, match):
        """Replace complex numbers with Unicode equivalents."""
        num = match.group(0)

        S = ('`5/8`', '`5/6`', '`4/5`', '`1/8`', '`1/5`', '`1/2`', '`1/4`',
             '`1/6`', '`1/3`', '`7/8`', '`3/8`', '`3/5`', '`3/4`', '`2/5`',
             '`2/3`', '`pi`', '`phi`', '`infinity`')
        R = ('⅝', '⅚', '⅘', '⅛', '⅕', '½', '¼',
             '⅙', '⅓', '⅞', '⅜', '⅗', '¾', '⅖',
             '⅔', 'π', 'φ', '∞')

        if num in S:
            num = R[S.index(num)]
        else:
            num = num.replace('`', '')

        yield match.start(), Number, num
    # -----------------------------------------------------------------------

    # Token Assignment
    # -----------------------------------------------------------------------
    tokens = {
        'root': [
            ## Comments
            (r''+ myComments, Comment),
            ## Submodules
            include('strings'),
            include('core'),
            include('nums')
        ],
        'core': [## Op Words
                 (r'\s(' + myOperatorWords + ')' + endOfToken,
                  Operator.Word),
                 ## Keywords
                 (r'\b(' + myKeywords + ')' + endOfToken, Keyword),

                 ## Data Types
                 (r'\b(' + myDatatypes +
                  ')(ish|esque|-like|s)?' + endOfToken,
                  Keyword.Type),

                 ## Constants
                 (r'\b('+ myConstants + ')' + endOfToken,
                  Name.Constant),

                 ## Op Symbols
                 (r'(' + myOperators + ')',
                  op_replace),

                 ## Punctuation
                 (r'(' + myPunctuation + ')',
                  Punctuation),

                 ## Names
                 (r'' + myFunctions, Name.Function),
                 (r'' + myVariables, Name.Variable)
        ],
        ## Strings
        'strings': [
            (r'"([^"])*"', String.Double),
            (r"'([^'])*'", String.Single),
        ],
        ## Numbers
        'nums': [
            (r'\d+(?![.Ee])', Number.Integer),
            (r'[+-]?\d*\.\d+([eE][-+]?\d+)?', Number.Float),
            (r'[+-]?\d+\.\d*([eE][-+]?\d+)?', Number.Float),
            (r'' + myComplexNumbers, num_replace)
        ],
    }
