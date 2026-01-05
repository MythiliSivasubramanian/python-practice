"""
Temperature Classifier :
Classifying the temperature as :
- Hot Day: temperature > 30°C
- Cold Day: temperature < 15°C
- Normal Weather: temperature between 15°C and 30°C
"""

# Prompting the user to enter temperature in celcius
temp = float(input("Enter temperature in °C: "))

# Classifying based on temperature conditions

if temp > 30:
    print("Hot Day")
elif temp < 15:
    print("Cold Day")
else:
    print("Normal Weather")
