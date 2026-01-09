def calculate_total_and_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average


def check_result(average):
    if average >= 40:
        return "PASS"
    else:
        return "FAIL"


def main():
    student_name = input("Enter student name: ")

    marks = []
    subjects = int(input("Enter number of subjects: "))

    for i in range(subjects):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    total, average = calculate_total_and_average(marks)
    result = check_result(average)

    print("\n----- Student Result -----")
    print("Name     :", student_name)
    print("Total    :", total)
    print("Average  :", round(average, 2))
    print("Result   :", result)


main()