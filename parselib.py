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


def star(parser):
    """repeat parsing until it's not possible anymore"""

    def parse(src, i):
        parsed = []
        while True:
            result = parser(src, i)
            if result is None:
                return i, parsed
            i, data = result
            parsed.append(data)

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


def cond(f, parser):
    """Apply a filter"""

    def parse(src, i):
        result = parser(src, i)
        if result is not None:
            i, data = result
            if f(data):
                return i, data

    return parse


"""
Custom combinators to ease parser development
"""


def allow(values, parser):
    return cond(lambda x: x in values, parser)


def blacklist(values, parser):
    return cond(lambda x: x not in values, parser)


def many(parser):
    """Similar to star(parser), but requires at least 1 result"""
    return cond(lambda results: len(results) > 0, star(parser))


def keyword(word):
    # parser for a sequence of determined characters
    letters = []
    for ch in word:
        letters.append(allow([ch], basechar))

    return concat(*letters)
