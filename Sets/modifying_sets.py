"""
Python Modifying Sets

- add()
- update()
- remove()
- discard()
- pop()

What is expected:
<<<<<<< HEAD
- Understand how sets change in-place
- Learn safe vs unsafe removal methods
=======
- Understanding how sets change in-place
- Learning safe vs unsafe removal methods
>>>>>>> c1775333139e66f3cc8415a465fc97185de9fb4d
"""

s = {1, 2, 3}

# add vs update
s.add(4)                  # adds one element
s.update([5, 6, 7])       # adds multiple elements
print("After add & update:", s)


# remove vs discard
s.remove(2)               # removes element (error if missing)
s.discard(100)            # no error even if element doesn't exist
print("After remove & discard:", s)


#pop()
popped_element = s.pop()  # removes a random element
print("Popped element:", popped_element)
print("Remaining set:", s)
