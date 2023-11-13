from lib.string_builder import *

def test_string_builder_adds_a_string():
    string = StringBuilder()
    string.add('hello')
    result = string.output()
    assert result == 'hello'

def test_string_builder_adds_multiple_strings():
    string = StringBuilder()
    string.add('hello')
    string.add(' world')
    string.add('!')
    result = string.output()
    assert result == 'hello world!'

def test_string_builder_returns_string_length_for_one():
    string = StringBuilder()
    string.add('hello')
    result = string.size()
    assert result == 5

def test_string_builder_returns_string_length_for_multiple():
    string = StringBuilder()
    string.add('hello')
    string.add(' world')
    string.add('!')
    result = string.size()
    assert result == 12