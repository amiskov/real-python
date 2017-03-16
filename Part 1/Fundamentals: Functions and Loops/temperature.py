def celsius_to_fahrenheit(temperature):
    """F = C * 9 / 5 + 32"""
    return temperature * 9 / 5 + 32


def fahrenheit_to_celsius(temperature):
    """C = (F - 32) * 5/9"""
    return (temperature - 32) * 5 / 9

print("72 degrees F = ", fahrenheit_to_celsius(72), 'degrees C')
print("37 degrees C = ", celsius_to_fahrenheit(37), 'degrees F')