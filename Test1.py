import os
# Example of LBYL:
# if os.path.exists("file.txt"):
#     with open("file.txt", "r") as f:
#         data = f.read()
# else:
#     print("File does not exist.")

# Example of EAFP:
# try:
#     with open("file.txt", "r") as f:
#         data = f.read()
# except FileNotFoundError:
#     print("File does not exist.")


# try:
#     x = 10 / 1  # No exception here
# except ZeroDivisionError:
#     print("Can't divide by zero!")
# else:
#     print("No exception occurred, so this runs!")


# try:
#     x = 10 / 0  # This will raise a ZeroDivisionError
# except ZeroDivisionError:
#     print("Can't divide by zero!")
# finally:
#     print("This will always execute, no matter what!")


# x = str(1.0)
# print(x)
# x[-1]= '2'
#
# text ="Enjoy the test"
# result =text.strip().split()[0]
# print(type(result))
#
# import math
# print(math.pi)


# f = open("name.txt", 'w')
# # line of code would go here
# print("Hello world1", file=f)
# f.writelines(["Hello,world2\n"])
# f.write("Hello world3")
# f.close()


# try:
#     x = int("zero")  # This will raise a ValueError because "zero" is not a valid integer
#     print(10 / x)
# except ZeroDivisionError:
#     print("div")
# except NameError:
#     print("name")
# except ValueError:
#     print("value")  # This will be executed
# except:
#     print("other")


# x= str(int('1.0'))
# print(x)
# x[-1] = '2'


# def test():
#     raise ValueError("This is a custom error message.")


# try:
#     test()
# except ValueError:
#     print("ValueError!")


# a: file object returned by open()
# b: file path or name
# c: mode in which the file is opened
# d: the content of the file after reading with read()

# b = "name.txt"  # File path
# c = "r"  # Mode (read mode)
# a = open(b, c)  # a is the file object
# d = a.read()  # d contains the content of the file
# print(d)
# a.close()


# # Using the 'with' statement
with open("example.txt", "w") as file:
    file.write("Hello, World!")  # Writing to the file
#
# # No need to explicitly close the file, it's automatically closed when the block ends
#
file = open("example.txt", "w")
try:
    file.write("Hello, World!")
finally:
    file.close()  # Manually closing the file
