try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Prevent division by zero
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers.txt!")

print("Finished.")

# Answers to the questions:

# 1. A ValueError will occur if the user enters a non-integer value, such as a string
#    or a floating-point number, when asked for the numerator or denominator.

# 2. A ZeroDivisionError will occur if the user enters 0 for the denominator,
#    as division by zero is not mathematically allowed.

# 3. Yes, we can avoid the ZeroDivisionError by adding a check before the division.
#    In the modified code, we check if the denominator is 0 and print an error message
#    before attempting to divide.
