# Python Quizzes

---

## Topic: Data Types

### Question 1 / 100 (Data types – type & mutability)

Which of the following are mutable and which are immutable?
Also, give the type for each.

```python
a = 10
b = 3.14
c = "hello"
d = [1, 2, 3]
e = (4, 5, 6)
f = {"x": 1, "y": 2}
g = {1, 2, 3}

<details> <summary>Show Answer</summary>
a: int, immutable
b: float, immutable
c: str, immutable
d: list, mutable
e: tuple, immutable
f: dict, mutable
g: set, mutable
</details>

## Topic: Operators

### Question 2 / 100 (Operators – tricky comparison)

What is the output of this code?
Explain why each output is what it is.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a is c)

