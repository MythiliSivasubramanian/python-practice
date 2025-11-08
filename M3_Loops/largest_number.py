# Finding the largest number in  the given input list

def find_largest(user_num):
    largest_num = 0
    for i in user_num:
        if i > largest_num:
            largest_num = i
    return largest_num


print("\nFinding the largest number among the given input\n")
while True:
    try:
        user_input = list(map(int,input("Enter the integers sparated by space : ").split(" ")))
        break
    except ValueError:
        print("Enter valid integers separated by space")

largest = find_largest(user_input)
print("Largest number is : ",largest)
