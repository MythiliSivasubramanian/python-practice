# Differnent ways to create a  Set

# Creating sets normally
print("\nCreating sets normally :")
my_sets_1 = {1,2,3}
print("My Set_1 is ",my_sets_1)

# Creating a set with duplicates
my_sets_2 = {1, 2, 2, 3, 3}
print("My Set_2 is ",my_sets_2) # Duplicates are removed automatically.

# Creating an empty set
my_sets_3 = set()
print("My Set_3 is ",my_sets_3)  # output : <class 'set'>
# set{} will create empty dictionary

# Creating a set from other iterables
# String becomes unique characters.  Order is not reliable
a = set([1, 2, 3, 3]) # {1, 2, 3}
print(a)
b = set((1, 2, 2))    # {1, 2}
print(b)
c = set("hello")      #  {'h', 'e', 'l', 'o'}
print(c)