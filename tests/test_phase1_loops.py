from learn_python.phase1_loops import countdown
from learn_python.phase1_loops import sum_list_for
from learn_python.phase1_loops import index_values
from learn_python.phase1_loops import min_and_max
from learn_python.phase1_loops import count_evens, count_evens_sum


def test_countdown_positive():
    assert countdown(5) == [5, 4, 3, 2, 1]


def test_countdown_zero_and_negative():
    assert countdown(0) == []
    assert countdown(-3) == []


def test_sum_list_for():
    assert sum_list_for([1, 2, 3]) == 6
    assert sum_list_for([]) == 0


def test_min_and_max():
    assert min_and_max([3, 1, 4, 2]) == (1, 4)
    assert min_and_max([7]) == (7, 7)
    assert min_and_max([]) == (None, None)


def test_count_evens():
    data = [1, 2, 3, 4, 6]
    assert count_evens(data) == 3
    assert count_evens_sum(data) == 3


def test_index_values():
    assert index_values(["a", "b", "c"]) == [(0, "a"), (1, "b"), (2, "c")]
    assert index_values(["x", "y"], start=1) == [(1, "x"), (2, "y")]
