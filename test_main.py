from main import reverse_long_words


def test_correct_words_reversed():
    assert reverse_long_words("Hello there") == "olleH ereht"


def test_correct_words_reversed_2():
    assert reverse_long_words("Hi there") == "Hi ereht"


def test_correct_result_one_word():
    assert reverse_long_words("Hello") == "olleH"
