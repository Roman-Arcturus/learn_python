# nested map + filter with lambdas,
def process_readings(readings: list[int]) -> list[int]:
    return list(
        map(
            lambda z: z * z,
            filter(
                lambda y: y > 0,
                readings
            )
        )        
    )    
    
# functional style comprehensions
def process_readings(readings: list[int]) -> list[int]:
    return [
        value * value
        for value in readings
        if value > 0
    ]    
    

input_data: list = [3, -5, 7, -7, 5]

print( process_readings(input_data) )


transactions = [
    {"id": 1, "amount": 100, "status": "ok"},
    {"id": 2, "amount": -50, "status": "ok"},
    {"id": 3, "amount": 200, "status": "fraud"},
    {"id": 4, "amount": 150, "status": "ok"},
]

"""Keeps only transactions with "status" == "ok"
Returns a list of their "amount" values squared
Decide whether a comprehension or map/filter chain is clearer
Input: list[dict] → Output: list[int]
Do not mutate input
Multi-line formatting for readability
"""

# functional style comprehensions
def f_comprehension(transfers: list[dict]) -> list[int]:
    return [
        value["amount"] * value["amount"]
        for value in transfers
        if value["status"] == "ok"
    ]    
    
# filter/map pipeline
def f_pipeline(transfers: list[dict]) -> list[int]:
    return list(
        map(
            lambda z: z["amount"] * z["amount"],
            filter(
                lambda y : y["status"] == "ok",
                transfers
            )
        )  
    )
    
    
print( f_comprehension(transactions) )
print( f_pipeline(transactions) )

