from slugify import slugify


def test_empty_string():
    assert slugify("") == ""


def test_hello_world():
    assert slugify("Hello World") == "hello-world"


def test_strip_and_collapse():
    assert slugify("Hello,  World!") == "hello-world"
    assert slugify("a--b") == "a-b"
