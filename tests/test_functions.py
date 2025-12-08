from learn_python.functions import add_numbers

# , describe_person, multiply_numbers, convert_celsius_to_fahrenheit


def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
