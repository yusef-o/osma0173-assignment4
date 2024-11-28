#Assignment 4 by Yusef Osman

print("Calculator App")
while True:
    print("Pick an operation")
    print("1 = ADD\n2 = SUB\n3 = MUL\n4 = DIV\nQ = QUIT")
    operation = input("Enter your operation: ")

    if operation == 'Q':
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "1":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == "2":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == "3":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == "4":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Cant divide by zero!")
    else:
        print("Invalid operation!")