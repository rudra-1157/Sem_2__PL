def convert_celsius_to_fahrenheit(celsius):
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
    return (celsius * 9/5) + 32