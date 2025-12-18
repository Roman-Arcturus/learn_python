from typing import List, Tuple, Optional, Sequence, Any


def countdown(n: int) -> List[int]:
    """
    Return a list counting down from n to 1 using a while-loop.
    If n <= 0, return an empty list.
    """
    result: List[int] = []
    current = n
    while current > 0:
        result.append(current)
        current -= 1
    return result


def sum_list_for(numbers: list[int]) -> int:
    total = 0
    for value in numbers:
        total += value
    return total


def min_and_max(values: list[int]) -> Tuple[Optional[int], Optional[int]]:
    if not values:
        return None, None
    it = iter(values)
    first = next(it)
    min_v = max_v = first
    for v in it:
        if v < min_v:
            min_v = v
        if v > max_v:
            max_v = v
    return min_v, max_v


def count_evens(numbers: list[int]) -> int:
    count = 0
    for x in numbers:
        if x % 2 == 0:
            count += 1
    return count


def count_evens_sum(numbers: list[int]) -> int:
    # generator expression that yields 1 for each even, then sum counts them
    return sum(1 for x in numbers if x % 2 == 0)


def index_values(seq: Sequence[Any], start: int = 0) -> list[Tuple[int, Any]]:
    result: list[Tuple[int, Any]] = []
    for i, value in enumerate(seq, start=start):
        result.append((i, value))
    return result
