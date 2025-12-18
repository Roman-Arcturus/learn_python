def mutate_in_place(values: list[int]) -> None:
    """
    Mutates the input list by doubling each element.
    """
    for i, value in enumerate(values):
        values[i] = value * 2


def transform(values: list[int]) -> list[int]:
    """
    Returns a new list with each element doubled.
    Does not mutate the input list.
    """
    return [
        value * 2
        for value in values
    ]


data = [1, 2, 3, 4]
alias = data  # shared identity

mutate_in_place(data)

print('data: ', data, ' alias:', alias)

result_transformed = transform(data)

print('data: ', data, ' alias:', alias, ' transformed:', result_transformed)
print('alias is data?: ', alias is data)
print('transformed is data?: ', result_transformed is data)

