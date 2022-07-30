"""Lexer for (Standardized) Pseudocode in Pygments."""
import re

from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import Punctuation, Text, Comment, \
    Operator, Keyword, Name, String, Number


class PseudocodeLexer(RegexLexer):
    """Lex our Pseudocode According to the Standard."""

    myComments = '\/\*.*\*\/|'                              # C Style Block
    myComments += '\/\/.*\n|#.*\n|'                         # C/Sh Style Line
    myComments += ';.*\n'                                   # Lisp Style Line
    myKeywords = 'read|obtain|get|'                         # Input
    myKeywords += 'print|display|show|'                     # Output
    myKeywords += 'compute|calculate|determine|'            # Compute
    myKeywords += 'set|initialize|init|let|'                # Initialize
    myKeywords += 'increment|bump|decrement|'               # Add/Sub one
    myKeywords += 'if|then|else|otherwise|'                 # If-Then-Else
    myKeywords += 'while|done|endwhile|do|'                 # (Do) While
    myKeywords += 'case|of|others|endcase|'                 # Case
    myKeywords += 'repeat|until|'                           # Repeat Until
    myKeywords += 'for|endfor|'                             # For
    myKeywords += 'call|exception|when|as|recurse'          # Program Flow
    myConstants = 'true|false|'                             # Booleans
    myConstants += 'nonexistant|unbound|missing|null|'      # Unbound
    myConstants += 'success|failure|'                       # Status
    myConstants += 'newline|beep|indent'                    # Formatting
    myDatatypes = 'number|string|character|boolean|'        # Basics
    myDatatypes += 'list|array|sequence|'                   # Collections
    myDatatypes += 'nothing|maybe|symbol|'                  # Abstractions
    myDatatypes += 'constant|operator|procedure|'           # Program
    myDatatypes += 'file|stream|pipe|port|'                 # OS
    myDatatypes += 'sum|difference|product|quotient|remainder' # Results
    myOperators =  '>\s|<\s|==|!=|<>|<=|>=|=|!<|!>|≡|≯|≮|≥|≤|≠|' # Comparison
    myOperatorWords = 'less than|more than|greater than|'      # Comparison Words 1
    myOperatorWords += 'equal to|different than|different from|'# Comparison Words 2
    myOperators += '¬|⊻|∨|∧|&&|\|\||'                               # Logical
    myOperatorWords += 'not|xor|and|or|exclusive|'               # Logical Words
    myOperators += '->|<-|→|←|'                             # Arrows
    myOperatorWords += 'resulting in|fed|right|left|'            # Arrows Words
    myOperators += '\^|\*|\+|-|\/|\%|×|÷'                  # Arithmetic
    myOperatorWords += 'plus|minus|times|divided by|modulo|'    # Arithmetic Words 1
    myOperatorWords += 'add|subtract|multiply|divide|'          # Arithmetic Words 2
    myOperatorWords += 'take the remainder of|raised to the|' # Artihmetic Words 3
    myOperatorWords += 'power|squared|cubed|root|square|cube'  # Arithmetic Words 4
    myPunctuation = '\(|\)|\,|:'                        # Basics
    myIntrinsics = '\[.*\S+.*\]\s'                                 # Brackets
    myComplexNumbers = '`.*\S.*`'
    
    name = 'Pseudocode (std)'
    aliases = ['pseudocode', 'pseudo', 'algorithm', 'algo']
    filenames = ['*.algo', '*.pseudocode']
    mimetypes = []
    flags = re.IGNORECASE

    def op_replace(lexer, match):
        """Replace ASCII digraphs with Unicode equivalents."""
        op = match.group(0)

        S = ('<=', '>=', '<>', '!=', '==', '->', '<-', '*', '/', '!<', '!>',
             '||', '&&')
        R = ('≤', '≥', '≠', '≠', '≡', '→', '←', '×', '÷', '≮', '≯', '∨', '∧')

        if op in S:
            op = R[S.index(op)]

        yield match.start(), Operator, op

    def num_replace(lexer, match):
        """Replace complex numbers with Unicode equivalents."""
        num = match.group(0)

        S = ('`5/8`', '`5/6`', '`4/5`', '`1/8`', '`1/5`', '`1/2`', '`1/4`',
             '`1/6`', '`1/3`', '`7/8`', '`3/8`', '`3/5`', '`3/4`', '`2/5`',
             '`2/3`', '`pi`', '`phi`')
        R = ('⅝', '⅚', '⅘', '⅛', '⅕', '½', '¼',
             '⅙', '⅓', '⅞', '⅜', '⅗', '¾', '⅖',
             '⅔', 'π', 'φ')

        if num in S:
            num = R[S.index(num)]
        else:
            num = num.replace('`', '')

        yield match.start(), Number, num
       

    tokens = {
        'root': [
                 (r''+ myComments, Comment),
                 include('strings'),
                 include('core'),
                 (r'(begin |end )(.+)',
                  bygroups(Keyword, Name.Function)),
                 (r'[a-zéàùçèÉÀÙÇÈ][a-z0-9éàùçèÉÀÙÇÈ_]*', Name.Variable),
                 include('nums'),
                 (r'[\s]+', Text),
                 (r'\d+/\d+', Number)
        ],
        'core': [  # Keywords
                 (r'\b(' + myKeywords + ')', Keyword),

                 # Data Types
                 (r'\b(' + myDatatypes + ')',
                  Keyword.Type),
            
                 # Constants
                 (r'\b('+ myConstants + ')',
                  Name.Constant),

                 # Operators
                 (r'(' + myOperators + ')',
                  op_replace),
                 (r' +(' + myOperatorWords + ') +',
                  Operator.Word),
            
                 # Punctuation
                 (r'(' + myPunctuation + ')',
                  Punctuation),

                 # Intrinsics
                 (r'' + myIntrinsics, Name.Builtin)
                ],

        'strings': [
                 (r'"([^"])*"', String.Double),
                 (r"'([^'])*'", String.Single),
                ],

        'nums': [
                 (r'\d+(?![.Ee])', Number.Integer),
                 (r'[+-]?\d*\.\d+([eE][-+]?\d+)?', Number.Float),
                 (r'[+-]?\d+\.\d*([eE][-+]?\d+)?', Number.Float),
                 (r'' + myComplexNumbers, num_replace)
                ],
        }
