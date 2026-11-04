students = []


def get_grade(mark):
    """Return the letter grade for a mark between 0 and 100."""
    if not 0 <= mark <= 100:
        raise ValueError("Mark must be between 0 and 100.")

    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 60:
        return "D"
    return "E"


def add_student():
    """Prompt for and add one student after validating the input."""
    while True:
        name = input("Enter student's name: ").strip()
        if name:
            break
        print("Name cannot be empty. Please try again.")

    while True:
        mark_text = input("Enter student's mark (0-100): ").strip()
        try:
            mark = float(mark_text)
        except ValueError:
            print("Please enter a numeric mark between 0 and 100.")
            continue

        if not 0 <= mark <= 100:
            print("Mark must be between 0 and 100.")
            continue
        break

    students.append({"name": name, "mark": mark})
    print(f"{name} was added successfully.")


def show_results():
    """Display every student's grade and the class statistics."""
    if not students:
        print("No student results to display.")
        return

    print(f"{'Name':<12} {'Mark':>6} {'Grade':>8}")
    print("-" * 28)
    for student in students:
        mark = student["mark"]
        print(f"{student['name']:<12} {mark:>6g} {get_grade(mark):>8}")

    marks = [student["mark"] for student in students]
    average = sum(marks) / len(marks)
    print(f"\nAverage: {average:.1f}")
    print(f"Highest: {max(marks):g}")
    print(f"Lowest: {min(marks):g}")


def main():
    while True:
        print("\n===== Student Grade Manager =====\n")
        print("1. Add Student")
        print("2. Show Results")
        print("3. Quit")

        try:
            choice = input("\nEnter your choice: ").strip()
        except EOFError:
            print("\nInput closed. Exiting.")
            break

        if choice == "1":
            try:
                add_student()
            except EOFError:
                print("\nInput closed. Exiting.")
                break
        elif choice == "2":
            show_results()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
