"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # Mark as finished when we successfully get an integer
    except ValueError:  # Catch the ValueError when the input is not a valid integer
        print("Please enter a valid integer.")
print("Valid result is:", result)
