from dbm import error
from logging import exception


def day_of_week_checker():
    # Ask the user to enter a number
    day_number = input("Enter a number (1 to 7): ")

    try:
        # Convert the input to an integer
        day_number = int(day_number)

        # Define a list of days
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Check if the input is within the valid range
        if 1 <= day_number <= 7:
            print(f"The day of the week is: {days[day_number - 1]}")
        else:
            print("Invalid input.")

    except ValueError:
        print("Invalid input.")


# Call the function
day_of_week_checker()
