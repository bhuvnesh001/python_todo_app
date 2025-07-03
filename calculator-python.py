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
        return "Error: Cannot divide by zero."

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def main():
    print("Welcome to Calculator!")
    
    operations = {
        '1': ('Add', add),
        '2': ('Subtract', subtract),
        '3': ('Multiply', multiply),
        '4': ('Divide', divide)
    }

    while True:
        print("\nSelect operation:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")

        choice = input("Enter choice (1/2/3/4): ")

        if choice in operations:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            operation_name, operation_func = operations[choice]
            result = operation_func(num1, num2)
            print(f"Result of {operation_name.lower()}ing {num1} and {num2} is: {result}")
        else:
            print("Invalid choice. Please select a valid operation.")

        again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for using Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
