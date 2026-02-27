"""
04_comparison_sorting_usage.py

- Tuple comparison rules
- Sorting tuples

"""

# 1. Tuple comparison

t1 = (1, 5)
t2 = (2, 5)

"""
Compares 1st element of t1 with first element of t2:
 - When 1st element of both tuples are equal, 
then second element of the tuples are compared and so on
 
"""
print(
      f"\n\nTuple comparisons :\n"
      f"Tuple t1 : {t1}\n"
      f"Tuple t2 : {t2}\n"
      )
print(f"t1 < t2 ?", t1 < t2) # Compares 1st element of t1 with first element of t2 

t3 = (1, 3)
t4 = (1, 7)
print(
      f"\nWhen 1st elements are same, 2nd element is compared:\n"
      f"t3 : {t3}\n"
      f"t4 : {t4}\n"
      )
print("t3 < t4 ?", t3 < t4)   # compares second element

# All elements of both tuples are same
t5 = (3, 9)
t6 = (3, 9)
print(
      f"\nCompare tuples with same elements:\n"
      f"t5 : {t5}\n"
      f"t6 : {t6}\n"
      )
print("t5 < t6 ?", t5 < t6)   # False

# 2. Sorting tuples

points = [(2, 3), (1, 5), (1, 2), (4, 1)] # List of tuples
print("\n\nOriginal points:", points)
print("Sorted points:", sorted(points))
