proper_t : tuple = 111, 222, 333
print(proper_t)

coord = (27, 56)
print(coord)

simple = 3, 4
print(simple)


t = (1, [2, 3])
print(t)

t[1].append(4)   # allowed — modifying the list inside
print(t)

def compute_basic_values() -> tuple[int, float, str]:
    a: int = 5
    b: float = 2.5
    c: str = "Python"

    sum_result = a + int(b)
    temperature = (a * b) + 1.5
    greeting = c + " developer"

    return sum_result, temperature, greeting