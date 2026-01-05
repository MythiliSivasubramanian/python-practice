"""
Triangle Validator :
Checking whether three given sides can form valid triangle.
- The sum of any two sides should be greater than the third side.
"""
# Prompting the user to enter the sides a,b,c of a triange
a = float(input("\nEnter side 1 of a triangle : "))
b = float(input("\nEnter side 2 of a triangle : "))
c = float(input("\nEnter side 3 of a triangle : "))

# Checking triangle validity
if a + b > c and a + c > b and b + c > a:
    print("\nValid Triangle")
else:
    print("\nInvalid Triangle")
