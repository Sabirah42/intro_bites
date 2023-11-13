from lib.check_codeword import *

def test_check_codeword_returns_correct_for_horse():
    result = check_codeword('horse')
    assert result == "Correct! Come in."

def test_check_codeword_returns_close_for_house():
    result = check_codeword('house')
    assert result == "Close, but nope."

def test_check_codeword_returns_close_for_hose():
    result = check_codeword('hose')
    assert result == "Close, but nope."

def test_check_codeword_returns_close_for_hopped():
    result = check_codeword('hopped')
    assert result == "WRONG!"

def test_check_codeword_returns_close_for_norse():
    result = check_codeword('norse')
    assert result == "WRONG!"