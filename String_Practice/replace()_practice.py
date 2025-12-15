
# PRACTICE: string.replace()

# Original string
my_string = "I like to eat Chocolates and Chocolates"

# Replace the FIRST occurrence of "Chocolates" with "Icecreams"
# Strings are immutable, so its not modified in place, instead new objects are created.
my_string = my_string.replace("Chocolates", "Icecreams", 1)
print(my_string)
# Output: I like to eat Icecreams and Chocolates

# Replace the FIRST space in the string with a "-"
print(my_string.replace(" ", "-", 1))
# Output: I-like to eat Icecreams and Chocolates

# Remove the substring "and" from the string
my_string = my_string.replace("and", "")
print(my_string)
# Output: I like to eat Icecreams  Chocolates
# There are now TWO spaces between Icecreams and Chocolates

# Replace the LAST space with a "," using rsplit() + join()
parts = my_string.rsplit(" ", 1)  # Split from the RIGHT at most 1 time
new_string = ",".join(parts)
print(new_string)
# Output: I like to eat Icecreams,Chocolates

# Method 2: Replace the LAST space using reverse() + replace() + reverse()
new_string2 = my_string[::-1].replace(" ", ",", 1)[::-1]
print(new_string2)
# Output: I like to eat Icecreams,Chocolates

# Summary:
# replace(old, new, count) replaces LEFT to RIGHT
# To replace from RIGHT:
#    - Use rsplit() + join(), or
#    - Reverse string, replace, reverse back
