## Code / Execution

def outer():
    value = 42  # local variable in outer scope

    def inner():
        return value  # references outer’s local variable

    return inner  # return the inner function

# Create closure
closure_func = outer()

# Call the inner function after outer has finished
result = closure_func()
print("Result:", result)

