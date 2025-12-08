def compute_basic_values() -> tuple[int, float, str]:
    a: int = 5
    b: float = 2.5
    c: str = "Python"

    sum_result = a + int(b)
    temperature = (a * b) + 1.5
    greeting = c + " developer"

    return sum_result, temperature, greeting
