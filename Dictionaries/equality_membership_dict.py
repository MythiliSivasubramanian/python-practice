"""
Demonstrating the differnce between (==) equality and
(is) identity operators using dictionaries. 
Dicts are created using {} and constructor dict()
"""

# Creating empty dictionaries using 2 methods. {} and dict()
a = {}
b = dict()

# Both dictionaries a and b have same content (both empty) but are different objects
print(f"id of A is {id(a)} and id of b is {id(b)}")
print(f"\nA == B : {a==b}")
print(f"\nA is B : {a is b}")


# Creating 2 empty dictionaries, using same method 
c = dict()
d = dict()

# Both dictionaries c and d have same content (both empty) but are different objects
print(f"id of c is {id(c)},Id of d is {id(d)}")
print(f"\nc == d : {c==d}")
print(f"\nc is d : {c is d}")

# Both a and e are dicts created using same method using {}. same content but different objects
e = {}
print(f"id of a is {id(a)},Id of e is {id(e)}")
print(f"\na == e : {a==e}")
print(f"\na is e : {a is e}")
