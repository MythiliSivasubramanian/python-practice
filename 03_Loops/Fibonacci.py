# To generate Fibonacci sequence up to given N numbers

def fibonacci(n):
    a, b = 0, 1
    count = 0

    # generate numbers until count reaches n
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1


if __name__ == "__main__":
    terms = int(input("Enter the number of terms: "))
    print("Fibonacci sequence:")
    fibonacci(terms)
