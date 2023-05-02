from parse import keywords, parse


def test_kw():
    let = keywords["let"]
    position, result = parse(let, "let")
    assert position == 3
    assert result == "let"
