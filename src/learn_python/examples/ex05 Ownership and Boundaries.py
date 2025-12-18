## Code / Execution

def process_owned(lst: list[int]) -> None:
    """
    Mutates the input list in place, assuming ownership.
    """
    for i in range(len(lst)):
        lst[i] *= 2


def process_borrowed(lst: list[int]) -> list[int]:
    """
    Returns a new list with doubled values.
    Does not mutate the input list.
    """
    return [x * 2 for x in lst]


data = [1, 2, 3]
alias = data  # shared reference

# Owned mutation
process_owned(data)

# Borrowed transformation
result = process_borrowed(data)
