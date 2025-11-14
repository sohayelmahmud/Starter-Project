def calculate_avg(score):
    if not score:
        return 0
    total_score = sum(score)
    avg = total_score / len(score)
    return avg

def calculate_grade(ind_marks):
    if ind_marks >= 80:
        return 'A+'
    elif ind_marks >= 70:
        return 'A'
    elif ind_marks >= 60:
        return 'A-'
    elif ind_marks >= 50:
        return 'B'
    elif ind_marks >= 40:
        return 'C'
    elif ind_marks >= 33:
        return 'D'
    else:
        return 'F'

def get_point(score):
    if score >= 80:
        return 5.00
    elif score >= 70:
        return 4.00
    elif score >= 60:
        return 3.50
    elif score >= 50:
        return 3.00
    elif score >= 40:
        return 2.00
    elif score >= 33:
        return 1.00
    else:
        return 0.00

def assign_final_grade_by_gpa(avg_gpa):
    if avg_gpa >= 5.00:
        return 'A+'
    elif avg_gpa >= 4.00:
        return 'A'
    elif avg_gpa >= 3.50:
        return 'A-'
    elif avg_gpa >= 3.00:
        return 'B'
    elif avg_gpa >= 2.00:
        return 'C'
    elif avg_gpa >= 1.00:
        return 'D'
    else:
        return 'F'






while True:
    try:
        marks_input = input("Enter marks (e.g. 79, 85, 69, 94): ")

        marks_list = [int(mark.strip()) for mark in marks_input.split(',')]

        if not marks_list or any(m < 0 or m > 100 for m in marks_list):
            print("Invalid input. Please enter valid marks (0-100) separated by commas.")
            continue

    except ValueError:
        print("Invalid input. Please ensure all inputs are valid numbers separated by commas.")
        continue

    point_list =[]
    individual_failed = False
    for mark in marks_list:
        point = get_point(mark)
        point_list.append(point)
        if point == 0.00:
            individual_failed = True


    if individual_failed:
        final_grade = "F"
        reason = " (Failed in one or more subjects.)"
        avg_gpa = 0.00
    else:
        total_points = sum(point_list)
        avg_gpa = total_points / len(point_list)
        final_grade = assign_final_grade_by_gpa(avg_gpa)
        reason = ""

    print("\n--- Individual Subject Result ---")
    for i, mark in enumerate(marks_list):
        grade = calculate_grade(mark)
        point = point_list[i]
        print(f"Subject {i+1}: Mark={mark}, Grade={grade}, Point={point:.2f}")

    print("\n--- Final Result ---")
    print(f"Total Subjects: {len(marks_list)}")
    print(f"Average Mark: {calculate_avg(marks_list):.2f}")
    print(f"Average GPA: {avg_gpa:.2f}")
    print(f"Final Grade: {final_grade}{reason}")



    while True:
        play_again = input("\nCalculate another grade? (y/n): ").lower().strip()
        if play_again == "n":
            print("Thanks. Goodbye!")
            exit()
        elif play_again == "y":
            print("Starting again.")
            print("................")
            break
        else:
            print("Invalid Input. please enter 'y' or 'n'.")
