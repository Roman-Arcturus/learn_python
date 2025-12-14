# ——— ——— ——— Defensive copying for mutable configuration ——— ——— ———

def make_allowed_checker(allowed: set[int]) -> callable[[int], bool]:
    allowed_copy = set(allowed)  # creates a new local reference to the input set

    def is_allowed(value: int) -> bool:
        return value in allowed_copy
        # is_allowed is having its own copy of allowed_copy set

    return is_allowed  

# demonstration:

# in config file:
exact_values_set = {111, 222, 333}

# closer to the beginning of some module
check_if_allowed = make_allowed_checker(exact_values_set)

# during the runtime code we use
tested_value = 333 # 333 is some value we need to check

if check_if_allowed(tested_value):
    # logic
    print("tested ok") # -> tested ok, correct
    
# for example is some module another coder for some reason wrote
exact_values_set = exact_values_set.add("bbb")

#and he tries to test some var using our closure
tested_value = "bbb"

if check_if_allowed(tested_value):
    # logic
    print("tested ok") # -> tested ok, correct.
    
# because mutation of the global exact_values_set won't affect our closure


