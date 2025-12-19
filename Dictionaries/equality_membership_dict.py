a = {}
b = dict()

print(f"id of A is {id(a)} and id of b is {id(b)}")
print(f"\nA == B : {a==b}")
print(f"\nA is B : {a is b}")

c = dict()
d = dict()

print(f"id of c is {id(c)},Id of d is {id(d)}")
print(f"\nc == d : {c==d}")
print(f"\nc is d : {c is d}")

e = {}
print(f"id of a is {id(a)},Id of e is {id(e)}")
print(f"\na == e : {a==e}")
print(f"\na is e : {a is e}")
