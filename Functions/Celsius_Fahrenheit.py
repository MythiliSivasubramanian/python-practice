"""
Temperature Conversion :
Two functions to convert temperatures:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
"""

# Function to convert Celsius to Fahrenheit
def c_to_f(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9/5) + 32


# Function to convert Fahrenheit to Celsius
def f_to_c(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5/9

# Predefined sample numbers
celsius_temp = 25
fahrenheit_temp = 77

# Printing the results
print(f"\n{celsius_temp}°C is {c_to_f(celsius_temp)}°F")
print(f"\n{fahrenheit_temp}°F is {f_to_c(fahrenheit_temp)}°C\n")