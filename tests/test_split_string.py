from strings.split_string import solution

def test_case_1_even_length_string():
    assert solution("asdfadsf") == ['as', 'df', 'ad', 'sf']

def test_case_2_odd_length_string():
    assert solution("abc") == ['ab', 'c_']
    assert solution("x") == ["x_"]

def test_mixed_examples():
    assert solution("asdfadsf") == ["as", "df", "ad", "sf"]
    assert solution("asdfads") == ["as", "df", "ad", "s_"]

def test_empty_string():
    assert solution("") == []