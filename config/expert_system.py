def evaluate_performance():
    print("Welcome to the Employee Performance Evaluation System")
    name = input("Enter Employee Name: ")

    try:
        quality = int(input("Rate Work Quality (1-5): "))
        punctuality = int(input("Rate Punctuality (1-5): "))
        teamwork = int(input("Rate Teamwork (1-5): "))
        attendance = int(input("Rate Attendance (1-5): "))
    except ValueError:
        print("Invalid input! Please enter numbers from 1 to 5.")
        return

    if not all(1 <= x <= 5 for x in [quality, punctuality, teamwork, attendance]):
        print("All scores must be between 1 and 5.")
        return

    # Calculate average score
    avg_score = (quality + punctuality + teamwork + attendance) / 4

    # Apply rules
    if avg_score >= 4.5:
        result = "Excellent"
    elif avg_score >= 3.5:
        result = "Good"
    elif avg_score >= 2.5:
        result = "Needs Improvement"
    else:
        result = "Poor"

    print(f"\nPerformance Report for {name}")
    print(f"Average Score: {avg_score:.2f}")
    print(f"Evaluation Result: {result}")

evaluate_performance()
