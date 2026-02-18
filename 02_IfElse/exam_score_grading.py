# Exam score Grading system
# function to find out the relevent grade
def grade_calc(mark):
    if mark > 100 or mark < 0:
        return f"Mark {mark} is Invalid. Please enter a valid Mark between 0 to 100"
    elif mark >= 90:
        return "Grade : A"
    elif mark >= 80:
        return "Grade : B"
    elif mark >= 70:
        return "Grade : C"
    elif mark >= 60:
        return "Grade : D"
    else:
        return "Grade : F"

# Validate the input
def validate_input():
    while True:
        try:
            user_mark = int(input("Enter the exam score between (0- 100) : "))
            return user_mark
        except ValueError:
            print("Enter a valid score between 0 - 100 ")

# function call
user_input_mark = validate_input()
grade = grade_calc(user_input_mark)

print(grade)

# Prompt user  if other exam scores to be checked.
choice = input("Would like to check the grade for another score? (yes/no) : ").lower()

while choice == "yes":

    user_input_mark = validate_input()
    grade = grade_calc(user_input_mark)
    print(grade)

    choice = input("Would like to check the grade for another score ? (yes/no) : ").lower()

print("Good day!")
