#Student Marks Analyzer
def marks_calc(a):
    total,average,high,low = 0,0,a[0],a[0]
    for i in a:
        total += i
    average = total / len(a)
    for count in a:
        if count > high:
            high = count
        elif count < low:
            low = count
    return total,average,high,low

while True:
    try:
        marks = list(map(float,input("Enter the Students marks separated by comma : ").split(",")))
        break
    except ValueError:
        print("Enter valid numbers separated by comma : ")

total_marks,avg_mark,high_mark,low_mark = marks_calc(marks)
print(f"Total Marks: {total_marks}\nAverage Marks: {round(avg_mark,2)}\nHighest Marks: {high_mark}\nLowest Marks: {low_mark}")
