
def get_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def main():
    print("STUDENT MARKS AND GRADE ANALYZER")

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    marks = []

    for i in range(1, 6):
        while True:
            try:
                mark = float(
                    input(f"Enter marks for subject {i} (0-100): ")
                )

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    average = total / len(marks)
    grade = get_grade(average)
    result = "PASS" if all(m >= 40 for m in marks) else "FAIL"

    print("\n--- STUDENT REPORT ---")
    print("Name:", name)
    print("Total:", total, "/ 500")
    print(f"Average: {average:.2f}%")
    print("Grade:", grade)
    print("Result:", result)


if __name__ == "__main__":
    main()
 