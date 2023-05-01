"""
Top-down, parser combinator based parser
Generate a syntactic tree from source code
"""

import parselib as lib

keywords = {}
for kw in "let", "mut", "if", "elif", "else", "while",\
        "for", "in", "do", "fn", "return":
    keywords[kw] = lib.keyword(kw)

operators = {}
for op in "+", "-", "/", "%", "//":
    operators[op] = lib.keyword(op)

# delimiters
paren_open = lib.keyword("(")
paren_close = lib.keyword(")")
bracket_open = lib.keyword("[")
bracket_close = lib.keyword("]")
brace_open = lib.keyword("{")
brace_close = lib.keyword("}")
