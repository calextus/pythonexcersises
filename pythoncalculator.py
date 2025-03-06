# this is a calculator task

#here i am defining the arithmatic functions
def add(a, b): # adds
    return a + b

def subtract(a, b): #sub
    return a - b

def multiply(a, b): #multiplies
    return a * b

def divide(a, b): #divides
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculator():
    while True:
        print("\nSimple Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        match choice:
            case "1":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {add(num1, num2)}")
            case "2":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {subtract(num1, num2)}")
            case "3":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {multiply(num1, num2)}")
            case "4":
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"Result: {divide(num1, num2)}")
            case "5":
                print("goodbye...")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    calculator()
