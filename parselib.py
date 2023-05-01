"""
Minimal parser combinator library

a parser is a function with the following signature:
(source: str, position: int) -> None or (position: int, object)
"""

def char(src, i):
    if i >= len(src):
        return None
    return i + 1, src[i]

