from lib.gratitudes import *

def test_gratitudes_adds_gratitude_to_formatted_list():
    gratitudes = Gratitudes()
    gratitudes.add('friends')
    result = gratitudes.format()
    assert result == "Be grateful for: friends"

def test_gratitudes_adds_multiple_gratitudes_to_formatted_list():
    gratitudes = Gratitudes()
    gratitudes.add('friends')
    gratitudes.add('family')
    gratitudes.add('employment')
    result = gratitudes.format()
    assert result == "Be grateful for: friends, family, employment"