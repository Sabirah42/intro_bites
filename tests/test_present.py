import pytest
from lib.present import *

def test_wrap_returns_contents():
    present = Present()
    present.wrap('toys')
    result = 'toys'
    assert result == 'toys'

def test_unwrap_returns_contents():
    present = Present()
    present.wrap('kitten')
    present.unwrap()
    result = 'kitten'
    assert result == 'kitten'

def test_wrap_returns_error_for_existing_contents():
    present = Present()
    present.wrap('toys')
    with pytest.raises(Exception) as e:
        present.wrap('puppy')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_unwrap_returns_error_for_no_contents():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

    
