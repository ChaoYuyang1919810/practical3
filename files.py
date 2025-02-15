# 1. Ask the user for their name and write it to a file
name = input("What is your name? ")

# Open 'name.txt' in write mode ('w') and write the name
file = open('name.txt', 'w')
file.write(name)
file.close()

# 2. Open 'name.txt' and read the name, then print it
file = open('name.txt', 'r')
name_from_file = file.read().strip()  # Read and remove any extra whitespace (like newlines)
file.close()

# Print the greeting message with the name
print(f"Hi {name_from_file}!")

# 3. Write code to open 'numbers.txt.txt', read the first two numbers.txt, and add them

# We assume that the numbers.txt.txt file is already created with the following contents:
# 17
# 42
# 400

with open('numbers.txt', 'r') as file:
    # Read the first two lines, convert them to integers and add them
    num1 = int(file.readline())  # Read the first number
    num2 = int(file.readline())  # Read the second number

# Output the sum of the first two numbers.txt
print(num1 + num2)  # Output: 59


# 4. Print the total for all numbers.txt in 'numbers.txt.txt'

with open('numbers.txt', 'r') as file:
    total = 0
    # Iterate through each line, convert to integer, and add to the total
    for line in file:
        total += int(line.strip())  # Strip to remove newline and convert to int

# Output the total sum
print(total)

