def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: Cannot divide by zero.")
        return None

def calculator():
    print("Simple Calculator")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return

    print("\nSelect operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        choice = int(input("Enter your choice (1/2/3/4): "))
    except ValueError:
        print("Error: Invalid input. Please enter a number.")
        return

    if choice not in [1, 2, 3, 4]:
        print("Error: Invalid choice. Please select a valid operation.")
        return

    if choice == 1:
        result = add(num1, num2)
        operator = "+"
    elif choice == 2:
        result = subtract(num1, num2)
        operator = "-"
    elif choice == 3:
        result = multiply(num1, num2)
        operator = "*"
    else:
        result = divide(num1, num2)
        operator = "/"

    if result is not None:
        print(f"\nResult: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()
