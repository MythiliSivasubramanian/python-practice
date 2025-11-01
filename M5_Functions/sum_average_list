#program to calculate sum und average of numbers in a list using function without buildin Sum() and average()

#function to calculate sum and average in a list
def sum_average_calc(a):
    sum, average = 0,0
    length_list = len(a)
    for numbers in a:
        sum = sum + numbers
    average = sum/length_list
    return  sum,average

#input from user
while True:
    try:
        user_numbers = list(map(float,input("Enter the numbers separated by comma : ").split(",")))
        break
    except ValueError:
        print("Please enter valid numbers separated by commas (e.g. 10,20,30): ")

#call function sum_average_calc
sum_result, average_result = sum_average_calc(user_numbers)

print(f"Sum = {sum_result}\nAverage = {average_result}")
