# Function to categorize grade based on score
def categorize_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
        return "Invalid score. Please enter a score between 0 and 100."

# Input score from user
try:
    score = float(input("Enter your score (0-100): "))
    grade = categorize_grade(score)
    print(f"Your grade is: {grade}")
except ValueError:
    print("Invalid input. Please enter a numeric value.")
