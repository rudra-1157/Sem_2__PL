def convert_fahrenheit_to_celsius(fahrenheit):
    if fahrenheit < -459.67:
        raise ValueError("Temperature cannot be below absolute zero (-459.67°F).")
    return (fahrenheit - 32) * 5/9