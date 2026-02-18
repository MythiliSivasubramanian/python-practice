# List comprehension that generates a list of cubes for numbers from 1 to 5.
cubes = [i**3 for i in range(1,6)]
print("\nCube of numbers from 1 to 5 is : ",cubes)


# Extract words longer than 4 characters. words = ["apple", "banana", "cherry", "kiwi", "grape"]
words = ["apple", "banana", "cherry", "kiwi", "grape"]
short_words = [word for word in words if len(word)>4]
print("\nInitial list is : ",words,"\nWords longer than 4 characters from the list is : ",short_words)

# Square only the even numbers. numbers = [1, 2, 3, 4, 5, 6]
numbers = [1, 2, 3, 4, 5, 6]
squared = [num ** 2 for num in numbers if num % 2 == 0]
print("\nInital list is : ",numbers,"\nSquare of only even numbers from list is : ",squared,"\n")
