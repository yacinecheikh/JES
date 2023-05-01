"""
Top-down, parser combinator based parser
Generate a syntactic tree from source code
"""

import parselib as lib
from parselib import keyword, oneof, opt, many, star

"""
static lexer tokens 
"""

keywords = {}
for kw in "let", "mut", "if", "elif", "else", "while",\
        "for", "in", "do", "fn", "return":
    keywords[kw] = keyword(kw)

operators = {}
for op in "+", "-", "/", "%", "//":
    operators[op] = keyword(op)

# delimiters
paren_open = keyword("(")
paren_close = keyword(")")
bracket_open = keyword("[")
bracket_close = keyword("]")
brace_open = keyword("{")
brace_close = keyword("}")

"""
spaces/indentation
"""

# all the blank characters can be used as separators
space = keyword(" ")
tab = keyword("\t")
newline = keyword("\n")

# separators can be optional or required
# example for optional spaces: f ( x ) (f(x))
# example for required spaces: x=1 y=2 (x=1y=2)
blank = oneof(space, tab, newline)

hardsep = many(blank)
softsep = star(blank)


"""
block parsers
"""


"""
expressions
"""

expression = lib.defer()

nested_expression = concat(paren_open, softspace, expression, softspace, )
