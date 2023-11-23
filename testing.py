#Testing test def
from test import sum

def test_sum():
    assert sum(1, 2) == 3
    assert sum(-1, 1) == 0
    assert sum(-1, -1) == -2