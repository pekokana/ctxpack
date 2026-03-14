from ctxpack.token import estimate_tokens


def test_token_small():

    assert estimate_tokens("abcd") == 1


def test_token_medium():

    assert estimate_tokens("abcdefgh") == 2


def test_token_large():

    text = "a" * 100

    assert estimate_tokens(text) == 25