""" Given a list of numbers, count how many elements are greater than the average of the list. Sample Input:
[10, 2, 5, 8, 20] Sample Output: 2
Explanation: Average = (10 + 2 + 5 + 8 + 20) / 5 = 9
Numbers greater than 9 → 10, 20  Count = 2 """

def main():
    user_list = list(map(int,input("Enter the items in list separated by comma : ").split(",")))

    average_numb = sum(user_list)/len(user_list)
    filtered_list = []
    for elements in user_list:
        if elements > average_numb:
            filtered_list.append(elements)
    print(len(filtered_list))

if __name__ == "__main__":
    main()
