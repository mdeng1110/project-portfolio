from main import main
from main import min_num
from main import max_num

def test_min_num():
    test_array = [1,2,3,4,5]
    assert min_num(test_array) == 1

def test_max_num():
    test_array = [1,2,3,4,5]
    assert max_num(test_array) == 5