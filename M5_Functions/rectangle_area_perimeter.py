# program to calculate area and perimeter of a rectangle using functions

# function to calculate area and perimeter
def rectangle_calc(a,b):
    area = a*b
    perimeter = 2 * (a+b)
    return area,perimeter

# validate if length and breath are valid integers
while True:
    try:
        length,width = map(float,input("Enter the length and breath as numbers, separated by comma : ").split(","))
        break
    except ValueError:
        print("Enter valid numbers as length and breath")

# call the function
rectangle_area, rectangle_perimeter = rectangle_calc(length,width)

#display the area and perimeter of the rectangle
print(f"Area of the Rectangle is {rectangle_area}\nPerimeter of the Rectangle is {rectangle_perimeter}")
