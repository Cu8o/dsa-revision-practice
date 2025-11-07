from fundamentals.parse_int_from_char import get_age

def test_parse_int_from_char():
    assert get_age("2 years old") == 2
    assert get_age("4 years old") == 4
    assert get_age("5 years old") == 5
    assert get_age("9 years old") == 9