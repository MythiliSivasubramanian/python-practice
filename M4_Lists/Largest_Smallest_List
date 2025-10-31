# Finding the Largest and Smallest Numbers in a List (without max() or min())

while True:
    try:
        input_count = int(input("How many numbers will you enter? "))
        break
    except ValueError:
        print("Enter a valid number : ")

user_list = []
for i in range(input_count):
    num = int(input(f"Enter number {i+1}: "))
    user_list.append(num)

largest = user_list[0]
smallest = user_list[0]

for n in user_list:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("\nNumbers entered:", user_list)
print("Largest number:", largest)
print("Smallest number:", smallest)
