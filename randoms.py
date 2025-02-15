import random

# line 1: What did you see on line 1?
# The output will be a random integer between 5 and 20, inclusive.
# The smallest number is 5, and the largest number is 20.
print(random.randint(5, 20))  # line 1

# line 2: What did you see on line 2?
# The output will be a random number from the range 3 to 10, but it will only produce odd numbers.txt (3, 5, 7, 9).
# The smallest number is 3, and the largest is 9.
# Could line 2 have produced a 4? No, because the step is 2, so it only produces odd numbers.txt.
print(random.randrange(3, 10, 2))  # line 2

# line 3: What did you see on line 3?
# The output will be a random floating-point number between 2.5 and 5.5.
# The smallest number is 2.5, and the largest number is 5.5.
print(random.uniform(2.5, 5.5))  # line 3

# Code to produce a random number between 1 and 100 inclusive:
print(random.randint(1, 100))  # random number between 1 and 100 inclusive
