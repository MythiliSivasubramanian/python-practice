# to find the no of positive, negative and zeros in a list
def nums_cat(a):
    count_positives,count_negatives,count_zeros = 0,0,0
    for i in a:
        if i == 0:
            count_zeros += 1
        elif i > 0:
            count_positives += 1
        else:
            count_negatives += 1
    return count_positives,count_negatives,count_zeros

while True:
    try:
        user_input = list(map(float,input("Enter the numbers separated by comma : ").split(",")))
        break
    except ValueError:
        print("Enter a valid numbers separated by comma (10,20,4.5,-2.9,0,33.6) : ")
postive_count,negative_count,zeros_count = nums_cat(user_input)

print(f"Positive numbers: {postive_count}\nNegative numbers: {negative_count}\nZeros: {zeros_count}")
