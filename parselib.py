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


def basechar(src, i):
    if i >= len(src):
        return None
    return i + 1, src[i]


"""
Parser combinators

These functions take parsers as input and generate new parsers
"""


def concat(*parsers):
    def parse(src, i):
        parsed = []
        for p in parsers:
            result = p(src, i)
            if result is None:
                return None
            i, data = result
            parsed.append(data)
        return i, parsed

    return parse


def oneof(*parsers):
    def parse(src, i):
        for p in parsers:
            result = p(src, i)
            if result is not None:
                return result

    return parse


def opt(parser):
    def parse(src, i):
        result = parser(src, i)
        if result is None:
            # successfully parsed nothing
            return i, None
        return result

    return parse


class defer:
    """Late binded parser. Needed for recursive parsing rules"""
    def __init__(self):
        self.parser = None
    def __call__(self, *args, **kwargs):
        self.parser(*args, **kwargs)


"""
functional programming
"""


def process(f, parser):
    def parse(src, i):
        result = parser(src, i)
        if result is not None:
            i, data = result
            return i, f(data)

    return parse


def allow(values, parser):
    def parse(src, i):
        result = parser(src, i)
        if result is None:
            return None
        i, data = result
        if data in values:
            return i, data


"""
Custom combinators to ease parser development
"""


def keyword(word):
    # parser for a sequence of determined characters
    letters = []
    for ch in word:
        letters.append(allow([ch], basechar))

    return concat(*letters)
