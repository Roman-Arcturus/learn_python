#  ——— ——— ——— Refactoring Exercise: From verbose pipeline to Pythonic clarity ——— ——— ———

numbers:list =[1, 7, -23, 6, 15, -79]

def is_positive(x: int) -> bool:
    return x > 0

def square(x: int) -> int:
    return x * x

def process_numbers(numbers: list[int]) -> list[int]:
    return list(
        map(
            square,
            sorted(
                filter(
                    is_positive,
                    numbers
                )
            )
        )
    )

print( process_numbers(numbers) )

def process_numbers(numbers: list[int]) -> list[int]:
    return list(
        map(
            square,
            list(   # redundant, as sorted() already materialize a list
                sorted(
                    filter(
                        is_positive,
                        numbers
                    )
                )
            )
        )
    )

def process_numbers(numbers: list[int]) -> list[int]:
    return [
        square(x)
        for x in sorted(numbers)
        if is_positive(x)
    ]

print( process_numbers(numbers) )