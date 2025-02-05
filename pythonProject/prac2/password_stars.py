password = input("Enter password:")
while len(password) < 6:
    print("Error")
    password = input("Enter password:")
for i in range(len(password)):

    print("*",end = "")