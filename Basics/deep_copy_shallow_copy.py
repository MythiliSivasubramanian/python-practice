"""   Create 3 variables referencing the same list. Mutate one. Check others."""
import copy

list_1 = list_2 = list_3 = [1, 2, 3]
# chained assignements. (all variables reference the same list)

list_shallowcopy = list_1.copy()   # Shallow copy duplicates only the top-level container, inner objects are shared.

list_deep = copy.deepcopy(list_1) #  Deep copy: creates a completely independent copy

list_1.append(4)   # List 1: [1, 2, 3, 4] List 2: [1, 2, 3, 4] List 3: [1, 2, 3, 4]

print(f"List 1: {list_1}\nList 2: {list_2}\nList 3: {list_3}\nList Shallowcopy: {list_shallowcopy}\nList Deepcopy: {list_deep}")

print(f"Id of List 1 : {id(list_1)}\nId of List 2 : {id(list_2)}\nId of List 3 : {id(list_3)}\nId of List 4 : {id(list_shallowcopy)}\nId of List 5 : {id(list_deep)}")
