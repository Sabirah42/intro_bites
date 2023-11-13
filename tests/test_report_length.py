from lib.report_length import *

def test_report_length_returns_5_for_hello():
    result = report_length('hello')
    assert result == "This string was 5 characters long."

def test_report_length_returns_11_for_hello_world():
    result = report_length('hello world')
    assert result == "This string was 11 characters long."

def test_report_length_returns_12_for_hello_world_special_chars():
    result = report_length('hello world!')
    assert result == "This string was 12 characters long."