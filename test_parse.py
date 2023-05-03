from parse import keywords, parse


def test_kw():
    let = keywords["let"]
    position, result = parse(let, "let")
    assert position == 3
    assert result == "let"


from parse import integer, decimal, power, number


def test_integer():
    position, result = parse(integer, "58")
    assert position == 2
    assert result == 58


def test_number():
    pos, result = parse(number, "5.0e2")
    assert pos == 5
    assert result == [5, 0, 2]


from parse import identifier, letter

def test_identifier():
    pos, result = parse(identifier, "variable15")
    assert pos == 10
    assert result == "variable15"
