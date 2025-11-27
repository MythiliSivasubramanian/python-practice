""" Given a list of numbers, return a new list containing only the even numbers. Sample Input: 4, 7, 2, 9, 6]
Sample Output: [4, 2, 6] """

def filter_even(list_1):
    even_list = []
    for items in list_1:
        if items % 2 == 0:
            even_list.append(items)
    return even_list

def main():
    user_list = list(map(int,input("Enter the numbers in a list : ").split(",")))
    new_list = filter_even(user_list)
    print(new_list)

if __name__ == "__main__":
    main()
