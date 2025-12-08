from learn_python.phase1_variables import compute_basic_values


def test_compute_basic_values():
    result = compute_basic_values()
    assert result[0] == 7
    assert round(result[1], 2) == 14.0
    assert result[2] == "Python developer"
