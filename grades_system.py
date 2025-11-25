student_grades = {}

def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a {grade}.")

def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"{name} with marks are updated {grade}.")
    else:
        print(f"{name} is not found !")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted.")
    else:
        print(f"{name} is not found !")

def display_all_student():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")
    else:
        print("No students found/added!!!")


def reverse_display_names():
    """
    Array Order Reversal:
    Converts dictionary keys to a list and reverses the order manually.
    """
    names_list = list(student_grades.keys())
    n = len(names_list)

    # Algorithm: Reversal in place
    for i in range(n // 2):
        names_list[i], names_list[n - i - 1] = names_list[n - i - 1], names_list[i]

    print("\n--- Students (Reverse Order) ---")
    for name in names_list:
        print(f"{name} : {student_grades[name]}")

def count_specific_grade_occurrence():
    """
    Array Counting:
    Counts how many students received a specific grade.
    """
    target = int(input("Enter grade to count occurrences: "))
    grades_list = list(student_grades.values())
    count = 0

    for grade in grades_list:
        if grade == target:
            count += 1

    print(f"Number of students with grade {target}: {count}")

def find_topper():
    """
    Finding the Maximum number in a set/list:
    Iterates through to find the highest grade.
    """
    if not student_grades:
        print("No data available.")
        return

    grades_list = list(student_grades.values())
    max_grade = grades_list[0]

    # Algorithm: Find Max
    for grade in grades_list:
        if grade > max_grade:
            max_grade = grade

    print(f"Highest Grade is: {max_grade}")
    # Find who has this grade
    for name, grade in student_grades.items():
        if grade == max_grade:
            print(f"Topper: {name}")

def get_unique_grades_ordered():
    """
    Removal of Duplicates from an ordered array:
    First sorts the grades, then removes duplicates manually.
    Also utilizes Tuple logic.
    """
    grades_list = list(student_grades.values())
    grades_list.sort() # Prepare ordered array

    if not grades_list:
        print("No grades available.")
        return

    unique_grades = []

    # Algorithm: Remove duplicates from ordered list
    if len(grades_list) > 0:
        unique_grades.append(grades_list[0])
        for i in range(1, len(grades_list)):
            if grades_list[i] != grades_list[i-1]:
                unique_grades.append(grades_list[i])

    # Using Tuple to display
    print("Unique Grades Achieved (Ordered):", tuple(unique_grades))

def partition_pass_fail():
    """
    Partitioning an array:
    Splits students into two lists based on a passing threshold.
    """
    threshold = 40 # Example pass mark
    passed = []
    failed = []

    names = list(student_grades.keys())

    for name in names:
        grade = student_grades[name]
        if grade >= threshold:
            passed.append(name)
        else:
            failed.append(name)

    print(f"\n--- Partition Results (Pass Mark: {threshold}) ---")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")

def find_kth_lowest_grade():
    """
    Finding the Kth smallest element:
    Sorts the list and finds the element at k-1 index.
    Demonstrates Set Operations to remove duplicates before ranking.
    """
    if not student_grades:
        print("Not enough data.")
        return

    # Set Operation: Convert to set to get unique grades only
    unique_grades_set = set(student_grades.values())
    sorted_grades = list(unique_grades_set)

    # Simple Sort logic (Bubble Sort) to stick to iteration constructs
    n = len(sorted_grades)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_grades[j] > sorted_grades[j+1]:
                sorted_grades[j], sorted_grades[j+1] = sorted_grades[j+1], sorted_grades[j]

    k = int(input(f"Enter rank (1 to {len(sorted_grades)}) for lowest grade: "))

    if 1 <= k <= len(sorted_grades):
        print(f"The {k}-th lowest unique grade is: {sorted_grades[k-1]}")
    else:
        print("Invalid rank entered.")

# --- MAIN LOOP ---

def main():
    while True:
        print('\n --------Student Grades Management System--------')
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View all students")
        print("--- Analysis Tools ---")
        print("5. View Reverse Order (Array Reversal)")
        print("6. Count Specific Grade (Array Counting)")
        print("7. Find Topper (Max Number)")
        print("8. View Unique Grades (Remove Duplicates)")
        print("9. Pass/Fail Report (Partitioning)")
        print("10. Find K-th Lowest Grade (Kth Smallest Element)")
        print("11. Exit")
        print('---------------.......----------------')

        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            name = input("Enter student name = ")
            try:
                grade = int(input("Enter student grade = "))
                add_student(name, grade)
            except ValueError:
                print("Grade must be an integer.")

        elif choice == 2:
            name = input("Enter student name = ")
            try:
                grade = int(input("Enter student grade = "))
                update_student(name, grade)
            except ValueError:
                print("Grade must be an integer.")

        elif choice == 3:
            name = input("Enter student name = ")
            delete_student(name)

        elif choice == 4:
            display_all_student()

        elif choice == 5:
            reverse_display_names()

        elif choice == 6:
            count_specific_grade_occurrence()

        elif choice == 7:
            find_topper()

        elif choice == 8:
            get_unique_grades_ordered()

        elif choice == 9:
            partition_pass_fail()

        elif choice == 10:
            find_kth_lowest_grade()

        elif choice == 11:
            print("Close the program...")
            break

        else:
            print("Invalid choice")

main()
