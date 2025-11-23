def c_to_f(c): return c * 9/5 + 32
def f_to_c(f): return (f - 32) * 5/9
def c_to_k(c): return c + 273.15

if __name__ == "__main__":
    print("1. C → F\n2. F → C\n3. C → K")
    choice = input("Choose: ")

    value = float(input("Enter value: "))

    if choice == "1":
        print(c_to_f(value))
    elif choice == "2":
        print(f_to_c(value))
    elif choice == "3":
        print(c_to_k(value))
