from parse import keywords, parse


def test_kw():
    let = keywords["let"]
    position, result = parse(let, "let")
    assert position == 3
    assert result == "let"


from parse import integer, decimal, power


def test_integer():
    position, result = parse(integer, "58")
    assert position == 2
    assert result == 58
