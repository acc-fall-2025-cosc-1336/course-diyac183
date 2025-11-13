import sys
sys.path.append("./")
from src.homework.g_lists_and_tuples.lists import get_lowest_list_value 

import sys
sys.path.append("./")
from src.homework.g_lists_and_tuples.lists import lowest_value

def test_get_lowest_list_value():
    assert lowest_value(8, 10, 1, 50, 20) == 1

    import sys
sys.path.append("./")
from src.homework.g_lists_and_tuples.lists import get_highest_list_value 

import sys
sys.path.append("./")
from src.homework.g_lists_and_tuples.lists import highest_value

def test_get_highest_list_value():
    assert highest_value(8, 10, 1, 50, 20) == 50
