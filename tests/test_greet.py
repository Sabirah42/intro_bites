from lib.greet import *

def test_greet_returns_hello_sabirah_for_sabirah():
    result = greet('Sabirah')
    assert result == 'Hello, Sabirah!'