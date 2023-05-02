"""
Top-down, parser combinator based parser
Generate a syntactic tree from source code
"""

import parselib as lib
from parselib import keyword, oneof, opt, many, star, concat, cond, tag

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
dot = keyword(".")
comma = keyword(",")

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

# literals: numbers, strings, arrays, objects
digits = [keyword(str(i)) for i in range(10)]
digit = oneof(*digits)

integer = many(digit)
decimal = concat(dot, integer)
power = concat(keyword("e"), integer)

# a literal integer can follow these syntaxes:
# 1 (at least integer part)
# .5 (at least decimal part)
# 1e5 (integer part with power)
# .5e4 (decimal part with power)
# however, e5 is read as the variable identifier "e5" (due to parsing precedence)
number = cond(lambda parts: len(parts), concat(opt(integer), opt(decimal), opt(power)))

base_expr = oneof(tag("num", number))  # literals

nested_expression = concat(paren_open, softsep, expression, softsep, )
