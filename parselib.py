"""
Minimal parser combinator library

a parser is a function with the following signature:
(source: str, position: int) -> None or (position: int, object)
"""

def char(src, i):
    if i >= len(src):
        return None
    return i + 1, src[i]

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

