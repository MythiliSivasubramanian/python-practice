#Generate a list of squares or cubes
numbers = list(range(1, 11))
squares = [x**2 for x in numbers]
cubes = [x**3 for x in numbers]
print("Squares:", squares)
print("Cubes:", cubes)
