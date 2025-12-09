from learn_python.p1_function import add_num

# , describe_person, multiply_numbers, convert_celsius_to_fahrenheit


def test_add_numbers():
    assert add_num(2, 3) == 5
    assert add_num(-1, 1) == 0
