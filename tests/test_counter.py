from lib.counter import *

def test_keeps_log_of_one_added_sums():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

def test_keeps_log_of_two_added_sums():
    counter = Counter()
    counter.add(5)
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 8 so far."

def test_keeps_log_of_multiple_added_sums():
    counter = Counter()
    counter.add(5)
    counter.add(5)
    counter.add(9)
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 22 so far."