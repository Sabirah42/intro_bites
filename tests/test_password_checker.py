import pytest
from lib.password_checker import *

def test_password_checker_returns_true_for_valid_password():
    checker = PasswordChecker()
    checker.check('12345678')
    result = True
    assert result == True

def test_password_checker_raises_exception_for_invalid_password():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check('123')
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

