# to find no of even and odd numbers in a list
def even_odd_cal(a):
    even_count,odd_count = 0,0
    for i in a:
        if i % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    return  even_count,odd_count

# validate input if its valid integer
while True:
    try:
       user_list = list(map(int, input("Enter the numbers separated by comma : ").split(",")))

       break
    except ValueError:
        print("Enter valid numbers separated by comma eg.(10,20,3,5.5): ")

no_even,no_odd = even_odd_cal(user_list)
print(f"There are {no_even} even numbers and {no_odd} odd numbers.")
