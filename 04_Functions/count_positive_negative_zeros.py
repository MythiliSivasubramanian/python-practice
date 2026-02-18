"""
Counting Positive, Negative, and Zero Numbers in a List
Prompting the user to enter numbers separated by commas,
then counting how many numbers are positive, negative, or zero.
"""

# Function to catagorize the numbers from input
def nums_cat(numbers):
    # Initalize all counts to 0
    count_positives,count_negatives,count_zeros = 0,0,0
    for num in numbers:
        if num == 0:
            count_zeros += 1
        elif num > 0:
            count_positives += 1
        else:
            count_negatives += 1
    return count_positives,count_negatives,count_zeros


# Prompting the user and validating input
while True:
    try:
        user_input = list(map(float,input("Enter the numbers separated by comma : ").split(",")))
        break
    except ValueError:
        print("Enter a valid numbers separated by comma (10,20,4.5,-2.9,0,33.6) : ")
        
# unpacking the counts from function
postive_count,negative_count,zeros_count = nums_cat(user_input)

# Printing results
print(f"Positive numbers: {postive_count}\nNegative numbers: {negative_count}\nZeros: {zeros_count}")
