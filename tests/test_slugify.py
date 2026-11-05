from slugify import slugify


def test_empty_string():
    assert slugify("") == ""


def test_hello_world():
    assert slugify("Hello World") == "hello-world"
