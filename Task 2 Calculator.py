#Calculator

print("Welcome! Calculator is started")

num1 =int(input("Enter N1: "))
num2 =int(input("Enter N2: "))
while True:
    #operation choice
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    operation = input("Enter the number corresponding to the operation: ")

    #condition
    if operation == '5':
        print("Calculator is stopped.")
        break
    if operation == '1':
        result = num1 + num2
        op_symbol = '+'
    elif operation == '2':
        result = num1 - num2
        op_symbol = '-'
    elif operation == '3':
        result = num1 * num2
        op_symbol = '*'
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            op_symbol = '/'
        else:
            result = "undefined (cannot divide by zero)"
            op_symbol = '/'
    else:
        print("Invalid operation. Please choose again.")
        continue

    # Display result
    print(f"{num1} {op_symbol} {num2} = {result}")

