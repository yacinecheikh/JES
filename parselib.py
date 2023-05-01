"""
Minimal parser combinator library

a parser is a function with the following signature:
(source: str, position: int) -> None or (position: int, object)
"""


"""
Base parser

This parser, although simple, helps guarantee the absence of bugs in further parsers,
by not manually writing index manipulation code.
"""
def char(src, i):
    if i >= len(src):
        return None
    return i + 1, src[i]

"""
Parser combinators

These functions take parsers as input and generate new parsers
"""
def concat(*parsers):
    def parser(src, i):
        parsed = []
        for p in parsers:
            result = p(src, i)
            if result is None:
                return None
            i, data = result
            parsed.append(data)
        return i, parsed
    return parser

"""
Custom combinators to ease parser development
"""
def keyword(word):
    letters = []
    for ch in word:
        letters.append(allow(ch, char))

    return concat(*letters)
