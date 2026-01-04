# Convert the temperature from celsicus to fahrenheit and kelvin
def convert_temperatures(celsius):
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    return fahrenheit, kelvin


print("=== Celsius to Fahrenheit & Kelvin Converter ===")

while True:
    try:
        c = float(input("Enter temperature in Celsius: "))
        f, k = convert_temperatures(c)
        print(f"Fahrenheit: {f:.2f}")
        print(f"Kelvin: {k:.2f}")
    except ValueError:
        print("Invalid number. Please try again.")

    again = input("Convert another? (y/n): ").lower()
    if again != "y":
        break
