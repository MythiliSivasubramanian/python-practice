""" Split "apple,banana,grape" into a list of fruits. Sample Input: "apple,banana,grape"
Sample Output: ['apple', 'banana', 'grape'] """

user_input = input('Enter a String, separated by comma eg("apple,banana,grape") : ')
print(list(user_input.split(",")))
print((user_input).split(","))
