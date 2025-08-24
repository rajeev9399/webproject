def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Subtract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def divide(x, y):
    """Divide Function"""
    if y == 0:
        return "Error! Division by zero."
    return x / y

def display_menu():
    """Display the calculator menu"""
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def get_user_choice():
    """Get user's choice"""
    while True:
        try:
            choice = int(input("Enter choice (1/2/3/4/5): "))
            if choice in [1, 2, 3, 4, 5]:
                return choice
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_numbers():
    """Get two numbers from the user"""
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numerical values.")

def main():
    """Main function to run the calculator"""
    print("Welcome to the Python Calculator!")
    while True:
        display_menu()
        choice = get_user_choice()
        if choice == 5:
            print("Exiting Calculator...")
            break
        num1, num2 = get_numbers()
        if choice == 1:
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == 2:
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == 3:
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == 4:
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")
        cont = input("Do you want to perform another calculation? (y/n): ")
        if cont.lower() != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
