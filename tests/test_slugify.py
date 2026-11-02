from slugify import slugify


def test_empty():
    assert slugify('') == ''


def test_hello_world():
    assert slugify('Hello World') == 'hello-world'
