"""
From a list of numbers:
if index is even → square the value
if index is odd → double the value
store results in a list (do NOT print inside loop)

"""

numbers = [1, 2, 3, 4, 5]

# Method 1: Traditional enumerate + .append
result = []
for index, value in enumerate(numbers):
    if index % 2 == 0:
        result.append(value ** 2)
    else:
        result.append(value * 2)
print(result)


# Method 2 : enumerate on list comprehension 

result = [value **2 if index % 2 == 0 
          else value * 2
          for index, value in enumerate(numbers)
          ]
print(result)
