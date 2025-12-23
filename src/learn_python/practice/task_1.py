original = [3, -2, 4, 0, 5, 8]

def is_even(x: int) -> bool:
    return x % 2 == 0

def is_positive(x: int) -> bool:
    return x > 0

def is_int(x: any) -> bool:
    return type(x) is int

def scale_by_10(x: int) -> int:
    return x * 10

def process_numbers(numbers: list[int]) -> list[int]:
    """
    Receives a list of integers and returns a newly created list of 
    positive, even integers scaled by 10. Validation is all-or-nothing. 
    For any kind of input mistype, returns an empty list []
    """
    
    #if input is not list early return
    if not isinstance(numbers, list):
        return []

    #first pass to validate that list elements all all ints
    """ 
    # an optimization for large lists. Will break the loop on the first mistype
    validated = []
    for n in numbers:
        if type(n) is not int:
            return [] # return from function directly
        validated.append(n)
    """
    validated = [
        n 
        for n in numbers
        if type(n) is int
    ]
    
    # non int elements were not copied, so lengths will differ
    if len(validated) != len(numbers):
        return []
    
    # all the type checkings are done at this point
    
    # second pass through safe list
    return [
        scale_by_10(n)
        for n in validated
        if is_positive(n) and is_even(n)
    ]
    

# faster version without separation of Interface/Logic
def process_numbers_v2(numbers: list[int]) -> list[int]:
    try:
        return [
            scale_by_10(n)
            for n in numbers
            if isinstance(n, int) and is_even(n) and is_positive(n)
        ]
    except TypeError:
        return []

print("original, global list:                ", original)
print("return of process_numbers(original):  ", process_numbers(original) )
print("original list after func is executed: ", original)
