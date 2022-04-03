"""Lexer for (Standardized) Pseudocode in Pygments."""
import re

from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import Punctuation, Text, Comment, \
    Operator, Keyword, Name, String, Number


class PseudocodeLexer(RegexLexer):
    """Lex our Pseudocode According to the Standard."""

    name = 'Pseudocode (std)'
    aliases = ['pseudocode', 'pseudo', 'algorithm', 'algo']
    filenames = ['*.algo', '*.pseudocode']
    mimetypes = []
    flags = re.IGNORECASE

    def op_replace(lexer, match):
        """Replace ASCII digraphs with Unicode equivalents."""
        op = match.group(0)

        S = ('<=', '>=', '<>', '<-', '^')
        R = ('≤',  '≥',  '≠',  '←',  '↑')

        if op in S:
            op = R[S.index(op)]

        yield match.start(), Operator, op

    tokens = {
        'root': [
                 (r'\/\*.*\*\/', Comment),
                 (r'(\/\/|#).*\n', Comment),
                 (r'\|', Comment),
                 (r'\{(.*)\}', Comment),
                 include('strings'),
                 include('core'),
                 (r'(begin +|end +)(.+$)',
                  bygroups(Keyword, Name.Function)),
                 (r'[a-zéàùçèÉÀÙÇÈ][a-z0-9éàùçèÉÀÙÇÈ_]*', Name.Variable),
                 include('nums'),
                 (r'[\s]+', Text)
        ],
        'core': [  # Keywords
                 (r'\b(read|obtain|get'              # Input
                  r'print|display|show'              # Output
                  r'compute|calculate|determine'     # Compute
                  r'set|initialize|init|let'         # Initialize
                  r'increment|bump|decrement'        # Add/Sub one
                  r'if[ _]then|if|then|else|endif'   # If-Then-Else
                  r'while|do|endwhile|done'          # (Do) While
                  r'case|of|others|endcase'          # Case
                  r'repeat[ _]until|repeat|until'    # Repeat Until
                  r'for|endfor'                      # For
                  r'call|exception|when|as|recurse'  # Program Flow
                  r')\s*\b', Keyword),

                 # Data Types
                 (r'\b(integer?|string?|float?|character?'
                  r'boolean?|array?|nothing)\s*\b',
                  Keyword.Type),

                 (r'\b(true|false|nil|null)\s*\b',
                  Name.Constant),

                 # Operators
                 (r'(<=|>=|<>|<-|\^|\*|\+|-|\/|<|>|=|\\\\|%'
                  r'←|↑|≤|≥|≠|÷|×|\.\.|\[|\]|\.|not|xor|and|or)',
                  op_replace),

                 (r'(\(|\)|\,|\;|:)',
                  Punctuation),

                 # Intrinsics
                 (r'\b(sqrt|pow|cos|sin|tan|arccos|arcsin|arctan'
                  r'arctan2|add|subtract|multiply|divide'
                  r'exp|ln|log'
                  r')\s*\b', Name.Builtin)
                ],

        'strings': [
                 (r'"([^"])*"', String.Double),
                 (r"'([^'])*'", String.Single),
                ],

        'nums': [
                 (r'\d+(?![.Ee])', Number.Integer),
                 (r'[+-]?\d*\.\d+([eE][-+]?\d+)?', Number.Float),
                 (r'[+-]?\d+\.\d*([eE][-+]?\d+)?', Number.Float)
                ],
        }
