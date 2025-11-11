from strings.word_spin import spin_words

def test_single_word_cases():
    assert spin_words("Welcome") == "emocleW"
    assert spin_words("to") == "to"
    assert spin_words("CodeWars") == "sraWedoC"

def test_multi_word_cases():
    assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
    assert spin_words("This sentence is a sentence") == "This ecnetnes is a ecnetnes"