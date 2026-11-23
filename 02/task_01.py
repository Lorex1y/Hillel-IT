# If the user enters not a number, it is his fault, not the program's

math_operations = ['+', '-', '*', '/']


first_number = float(input("Enter a first number: "))
second_number = float(input("Enter a second number: "))


math_operation = input("Enter a math operation [+, -, *, /]: ")
if math_operation not in math_operations:
    print("Invalid math operation")
    exit()

match math_operation:
    case '+':
        print(f"{first_number} + {second_number} = {first_number + second_number}")
    case '-':
        print(f"{first_number} - {second_number} = {first_number - second_number}")
    case '*':
        print(f"{first_number} * {second_number} = {first_number * second_number}")
    case '/':
        try:
            print (f"{first_number} / {second_number} = {first_number / second_number}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed")