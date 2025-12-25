def determine_temperature(tc: float) -> str:
    result: str = ""
    if tc < 10:
        result = "cold"
    elif 10 <= tc <= 25:
        result = "warm"
    else:
        result = "hot"
    return result


def categorize_speed(kmh: float) -> str:
    if kmh < 0:
        return "invalid"
    if kmh < 1:
        return "stopped"
    if kmh <= 50:
        return "slow"
    if kmh <= 120:
        return "normal"

    return "fast"


def determine_temperature_2(tc: float) -> str:
    if tc < 10:
        return "cold"
    if tc <= 25:
        return "warm"

    return "hot"


def explain_value(x: float) -> str:
    if x < 0:
        return "negative"
    elif x == 0:
        return "zero"
    else:
        return "positive"


def assess_weather(temp_c: float, is_raining: bool) -> str:
    if is_raining:
        if temp_c < 5:
            return "cold and rainy"
        if temp_c <= 20:
            return "rainy"

        return "warm and rainy"

    if temp_c < 5:
        return "cold"
    if temp_c <= 20:
        return "mild"

    return "warm"


# print (categorize_speed(23.45))
# print( determine_temperature(22) )
# print ( determine_temperature_2(12.23) )
# print( explain_value(12.45) )

print(assess_weather(12.34, False))
