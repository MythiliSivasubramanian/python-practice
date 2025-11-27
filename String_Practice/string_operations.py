import sys
a = "A,B,C"
b = ""
print(f"a is {a}   b is {b}.  Size:  a : {sys.getsizeof(a)} b: {sys.getsizeof(b)}")
print(f"Locations   a : {id(a)}  b: {id(b)}")

for elements in a:
    b += a
    print(f"\na is {a} and b is {b}   Size of a is : {sys.getsizeof(a)}. Location is a is {id(a)}  Size of b is : {sys.getsizeof(b)}. Location is {id(b)}")
print(f"\na is : {a}\n Size of a is : {sys.getsizeof(a)}. Location of a is : {id(b)}.    b is : {b}\n Size of b is : {sys.getsizeof(b)}. Location of b is : {id(b)}")
