# ——— ——— ——— Exercise 15 — Function as a Value ——— ——— ———

def squared(x: int | float) -> int | float:
    return x * x

f_squared = squared

# ——— ——— ——— Exercise 16 — Function as Parameter ——— ——— ———

def triple(x: int | float) -> int | float:
    return x * 3

def apply(x: int | float, fn:callable) -> int | float:
    return fn(x)

result_1 = apply(5, squared)
result_2 = apply(5, triple)

print(result_1, ' ', result_2)

# ——— ——— ——— Exercise 17 — Function Dispatch Table ——— ——— ———

ops: dict = {
    "square": squared,
    "triple": triple,
}

def compute(x: int | float, mode: str) -> int | float | None:
    fn = ops.get(mode)
    if fn is None:
        return None
    
    return fn(x)

# advanced variant
def compute(x, mode):
    return ops.get(mode, lambda _: None)(x)


result = compute(7, "asd")

#print(result)

