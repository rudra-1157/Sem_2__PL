def convert_celsius_to_kelvin(celsius):
    if celsius < -273.15:
        raise ValueError("Temperature cannot be below absolute zero (-273.15°C).")
    return celsius + 273.15