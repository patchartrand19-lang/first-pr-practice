from stringutils import is_palindrome, reverse_words


def test_is_palindrome_true():
    assert is_palindrome("A man a plan a canal Panama")


def test_is_palindrome_false():
    assert not is_palindrome("Hello world")


def test_reverse_words():
    assert reverse_words("hello world") == "world hello"
