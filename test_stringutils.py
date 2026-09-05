from stringutils import is_palindrome, reverse_words, truncate


def test_is_palindrome_true():
    assert is_palindrome("A man a plan a canal Panama")


def test_is_palindrome_false():
    assert not is_palindrome("Hello world")


def test_reverse_words():
    assert reverse_words("hello world") == "world hello"


def test_truncate_no_op_when_within_limit():
    assert truncate("hello", 10) == "hello"


def test_truncate_shortens_and_adds_ellipsis():
    assert truncate("hello world", 8) == "hello..."
