# Addition Function
def add_numbers(num1, num2):
    return num1 + num2

# Subtraction Function
def subtract_numbers(num1, num2):
    return num1 - num2

# Multiplication Function
def multiply_numbers(num1, num2):
    return num1 * num2

# Division Function 
def divide_numbers(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero!"
    return num1 / num2

# Basic displaying function...
def calculator():
    print("Welcome to Simple Calculator!")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    while True:
        choice = input("Enter your choice (1/2/3/4/5): ")
        
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print("Result:", add_numbers(num1, num2))
            elif choice == '2':
                print("Result:", subtract_numbers(num1, num2))
            elif choice == '3':
                print("Result:", multiply_numbers(num1, num2))
            elif choice == '4':
                print("Result:", divide_numbers(num1, num2))
        elif choice == '5':
            print("Thanks for using my Calculator! Use it again!!!")
            break
        else:
            print("Invalid input. Please enter a valid choice.")

# Main
def main():
    calculator()

# Program entrance
if _name_ == "_main_":
    main()
