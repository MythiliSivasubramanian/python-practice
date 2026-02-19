import sys
s1 = "Python"
s2 = "Python"
print(f"No Changes:         S1 : {s1}               S2  : {s2}")
print(f"Size of:            S1 : {sys.getsizeof(s1)}                   S2  : {sys.getsizeof(s2)}")
print(f"Location:           S1 : {id(s1)}           S2 : {id(s2)}")
s1 += "3"
print(f"\nAdd 3 to S1:        S1 : {s1}              S2 : {s2}")
print(f"Size of:            S1 : {sys.getsizeof(s1)}                   S2  : {sys.getsizeof(s2)}")
print(f"Location:           S1 : {id(s1)}           S2 : {id(s2)}")

s1 = "Python"
print(f"\nReassign as Python to S1:     S1 : {s1}       S2 is : {s2}")
print(f"Size of:            S1 : {sys.getsizeof(s1)}                   S2  : {sys.getsizeof(s2)}")
print(f"Location:           S1 : {id(s1)}           S2 : {id(s2)}")

s1 = "Pythons"
print(f"Reassign Pythons to S1:     s1 : {s1}        S2 is : {s2}")
print(f"Size of:            S1 : {sys.getsizeof(s1)}                   S2  : {sys.getsizeof(s2)}")
print(f"Location:           S1 : {id(s1)}           S2 : {id(s2)}")
