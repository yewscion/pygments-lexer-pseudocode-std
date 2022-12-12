"""Lexer for Pseudotaxus Pseudocode in Pygments."""
import re

from pygments.lexer import RegexLexer, include, bygroups
from pygments.token import Punctuation, Text, Comment, \
    Operator, Keyword, Name, String, Number

class PseudotaxusLexer(RegexLexer):
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
    myKeywords = 'read|obtain|get|from|take|copy|expect|'
    ## Output
    myKeywords += 'print|display|show|save|return|'
    ## Compute
    myKeywords += 'compute|execute|calculate|determine|append|to|over|'
    ## Initialize
    myKeywords += 'set|initialize|init|let|is|has|contains|be|'
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
    myKeywords += 'call|calling|exception|as|recurse|begin|end|rhizome|on|'
    ## Abstractions
    myKeywords += 'this|that|except|in|at|with|'
    ## Type Ops
    myKeywords += 'convert|cast|ensure|expecting|'
    ## Structure Ops
    myKeywords += 'where|containing|'
    ## Uncertainty
    myKeywords += 'either'
    # -----------------------------------------------------------------------

    # Constants
    # -----------------------------------------------------------------------
    ## Booleans
    myConstants = 'true|false|'
    ## Unbound
    myConstants += 'nonexistant|unbound|missing|null|'
    ## Status
    myConstants += 'success|failure|succeeds|fails|found|'
    ## Formatting
    myConstants += 'newline|beep|indent|'
    ## Assumptions
    myConstants += 'user|screen|system|'
    ## Types of Procedures
    myConstants += 'datum|data|caclulation|calculations|action|actions'
    # -----------------------------------------------------------------------

    # Datatypes
    # -----------------------------------------------------------------------
    ## Basics
    myDatatypes = 'number|word|phrase|item|identifier|'
    ## Extended Boolean
    myDatatypes += 'truthy|falsey|'
    ## Collections
    myDatatypes += 'sequence|every|each|member|index|'
    ## Abstractions
    myDatatypes += 'nothing|maybe|symbol|many|any|object|'
    ## Programming
    myDatatypes += 'constant|operator|procedure|argument|parameter|'
    ## OS
    myDatatypes += 'file|stream|pipe|port|line|interrupt|'
    ## Programming Refs
    myDatatypes += 'value|name|result|message|field|an|a|the|'
    ## Primitive Types
    myDatatypes += 'integer|character|boolean|floating-point|fixed-point|'
    myDatatypes += 'pointer|reference|enum|enumeration|'
    ## Composite Types
    myDatatypes += 'structure|array|record|tuple|string|union|variant|'
    myDatatypes += 'coproduct|t-union|sum-type|product-type|'
    ## Abstract Data Types
    myDatatypes += 'list|set|suite|stack|queue|tree|'
    myDatatypes += 'graph|heap|grid|hash-map|'
    ## Concrete Data Types
    myDatatypes += 'priority-queue|binary-tree|quad-tree|cons-list|'
    myDatatypes += 'doubly-linked-list|k-d-tree|skip-list|linked-list|matrix|'
    myDatatypes += 'lookup-table|bit-array|variable-length-array|dynamic-array|'
    myDatatypes += 'gap-buffer|zipper|b-tree|binary-search-tree|b-plus-tree|'
    myDatatypes += 'binary-heap|binomial-heap|radix-tree|suffix-tree|'
    myDatatypes += 'ternary-tree|m-ary-tree|k-ary-tree|and-or-tree|spqr-tree|'
    myDatatypes += 'in-tree|segment-tree|range-tree|bin|finger-tree|'
    myDatatypes += 'bloom-filter|count-min-sketch|adjacency-list|adjacency-matrix|'
    myDatatypes += 'decision-tree|directed-graph|undirected-graph|forest|'
    myDatatypes += 'link-cut-tree|dynamic-tree|array-list|a-list|'
    ## Plural Basics
    myDatatypes += 'numbers|words|phrases|items|identifiers|'
    ## Plural Collections
    myDatatypes += 'sequences|members|indices|'
    ## Plural Abstractions
    myDatatypes += 'nothings|maybes|symbols|objects|'
    ## Plural Programming
    myDatatypes += 'constants|operators|procedures|arguments|parameters|'
    ## Plural OS
    myDatatypes += 'files|streams|pipes|ports|lines|interrupts|'
    ## Plural Programming Refs
    myDatatypes += 'values|names|results|messages|fields|'
    ## Plural Primitive Types
    myDatatypes += 'integers|characters|booleans|floating-points|fixed-points|'
    myDatatypes += 'pointers|references|enums|enumerations|'
    ## Plural Composite Types
    myDatatypes += 'structures|arrays|records|tuples|strings|unions|'
    myDatatypes += 'variants|coproducts|t-unions|sum-types|product-types|'
    ## Plural Abstract Data Types
    myDatatypes += 'lists|sets|suites|stacks|queues|trees|'
    myDatatypes += 'graphs|heaps|grids|hash-maps|'
    ## Plural Concrete Data Types
    myDatatypes += 'priority-queues|binary-trees|quad-trees|cons-lists|'
    myDatatypes += 'doubly-linked-lists|k-d-trees|skip-lists|linked-lists|'
    myDatatypes += 'matrices|lookup-tables|bit-arrays|variable-length-arrays|'
    myDatatypes += 'dynamic-arrays|gap-buffers|zippers|b-trees|'
    myDatatypes += 'binary-search-trees|b-plus-trees|binary-heaps|binomial-heaps|'
    myDatatypes += 'radix-trees|suffix-trees|ternary-trees|m-ary-trees|'
    myDatatypes += 'k-ary-trees|and-or-trees|spqr-trees|in-trees|segment-trees|'
    myDatatypes += 'range-trees|bins|finger-trees|bloom-filters|'
    myDatatypes += 'count-min-sketches|adjacency-lists|adjacency-matrices|'
    myDatatypes += 'decision-trees|directed-graphs|undirected-graphs|forests|'
    myDatatypes += 'link-cut-trees|dynamic-trees|array-lists|a-lists|'
    ## Imprecise Basics
    myDatatypes += 'numberish|numbery|stringish|stringy|characterish|'
    myDatatypes += 'charactery|booleanish|booleany|'
    ## Imprecise Collections
    myDatatypes += 'listish|listy|arrayish|array-y|sequenceish|'
    myDatatypes += 'sequencey|memberish|membery|indexish|indexy|'
    ## Imprecise Abstractions
    myDatatypes += 'nothingish|nothingy|maybeish|maybe-y|symbolish|'
    myDatatypes += 'symboly|objectish|objecty|'
    ## Imprecise Programming
    myDatatypes += 'constantish|constanty|operatorish|operatory|'
    myDatatypes += 'procedureish|procedurey|argumentish|argumenty|'
    myDatatypes += 'parameterish|parametery|'
    ## Imprecise OS
    myDatatypes += 'fileish|filey|streamish|streamy|pipeish|'
    myDatatypes += 'pipey|portish|porty|lineish|liney|'
    myDatatypes += 'interruptish|interrupty'
    # -----------------------------------------------------------------------

    # Algorithms
    # -----------------------------------------------------------------------
    ## Arithmetic
    myAlgorithms = 'sum|difference|product|quotient|remainder|modulus|'
    myAlgorithms += 'sign|reciprocal|magnitude|logarithm|'
    ## Statistics
    myAlgorithms += 'average|mean|median|mode|range|'
    ## Extrema
    myAlgorithms += 'max|maximum|min|minimum|maxima|minima|ceiling|floor|'
    ## Search Sort Filter
    myAlgorithms += 'sort|reverse|search|find|filter in|filter out|'
    ## Grade Scan Map Reduce
    myAlgorithms += 'grade up|grade down|scan|map|reduce|expand|replicate|'
    ## Membership
    myAlgorithms += 'depth|match|tally|enlist|membership|pick|drop|take|iota'
    
    
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
    myOperatorWords = 'less than|more than|greater than|equals|'
    ## Comparison Words 2
    myOperatorWords += 'equal to|different than|different from|'
    ## Logical Words
    myOperatorWords += 'not|xor|and|or|exclusive|'
    ## Arrows Words
    myOperatorWords += 'resulting in|fed|right|left|'
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
    myPunctuation = '[(),:.?[\]{}\\\\]'
    ## Brackets
    myFunctions = '\[.*\S+.*\](?:\s|[,.:?])'
    ## Capital Initial
    myVariables = '[A-Z]\w*'
    ## Scientific Notation
    myComplexNumbers = '`.*\S.*`'
    ## Ordinals
    myOrdinals = '\d(?:th|st|nd|rd|d)'
    ## Ordinal Words
    myOrdinalWords = 'first|second|third|fourth|fifth|sixth|seventh|eighth|'
    myOrdinalWords += 'ninth|tenth|eleventh|twelfth|thirteenth|fourteenth|'
    myOrdinalWords += 'fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|'
    myOrdinalWords += 'twentieth|thirtieth|fortieth|fiftieth|sixtieth|'
    myOrdinalWords += 'seventieth|eightieth|nintieth|hundreth|thousandth|'
    myOrdinalWords += 'millionth|billionth|trillionth|quadrillionth|'
    myOrdinalWords += 'quintillionth|sextillionth|septillionth|octillionth|'
    myOrdinalWords += 'nonillionth|decillionth|undecillionth|duodecillionth'
    ## Number Words
    myNumberWords = 'one|two|three|four|five|six|seven|eight|nine|ten|eleven|'
    myNumberWords += 'twelve|thirteen|fourteen|fifteen|sixteen|seventeen|'
    myNumberWords += 'eighteen|ninteen|twenty|thirty|forty|fifty|sixty|seventy|'
    myNumberWords += 'eighty|ninety|hundred|thousand|million|billion|trillion|'
    myNumberWords += 'quadrillion|quintillion|sextillion|septillion|octillion|'
    myNumberWords += 'nonillion|decillion|undecillion|duodecillion|googol|centillion'
    ## End of Token Indicators
    endOfToken = '(?= |\.|\n|:|,)'
    ## Normal Text, unhighlighted
    myText = '( +)|[a-z]\w*'
    # -----------------------------------------------------------------------

    # Metadata
    # -----------------------------------------------------------------------
    name = 'Pseudotaxus Pseudocode'
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
        R = ('≤', '≥', '≠', '≠', '=', '→', '←', '×', '÷', '≮', '≯', '∨', '∧')

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
                 (r'\s+(' + myOperatorWords + ')' + endOfToken,
                  Operator.Word),

                 ## Algorithms
                 (r'\s+(' + myAlgorithms + ')' + endOfToken,
                  Name.Function),
            
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


                 ## Names
                 (r'' + myFunctions, Name.Function),
                 (r'' + myVariables, Name.Variable),
                 ## Punctuation
                 (r'(' + myPunctuation + ')',
                  Punctuation),
                 (r'(' + myText + ')',
                  Text)
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
            (r'' + myComplexNumbers, num_replace),
            (r'' + myOrdinals, Number),
            (r'' + myOrdinalWords, Number),
            (r'' + myNumberWords, Number)
        ],
    }
