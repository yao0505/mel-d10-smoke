from linecount import count_lines


def test_empty():
    assert count_lines("") == 0


def test_single_line():
    assert count_lines("hello") == 1
    assert count_lines("hello\n") == 1


def test_multi_line():
    assert count_lines("a\nb\nc") == 3
    assert count_lines("a\nb\nc\n") == 3
