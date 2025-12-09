def add(a,b):
    return a + b    
def sub(a,b):
    return a - b    
def mult(a,b):      
    return a * b    
def divi(a,b):    
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b            
def power(a,b):    
    return a ** b    
def sqrt(a):    
    if a < 0:
        raise ValueError("Cannot take square root of negative number.")
    return a ** 0.5    
def fact(n):    
    if n < 0:
        raise ValueError("Cannot take factorial of negative number.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def mod(a,b):    
    return a % b  
check = "yes"  
while check == "yes":

    print("Calculator Menu.")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Factorial")
    print("8. Modulus")
    print("9. Exit")
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9): ")   

    if choice in ['1', '2', '3', '4', '5', '8']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {sub(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {mult(num1, num2)}")
    elif choice == '4':
        try:
            print(f"{num1} / {num2} = {divi(num1, num2)}")
        except ValueError as e:
            print(e)
    elif choice == '5':
        print(f"{num1} ^ {num2} = {power(num1, num2)}")
    elif choice == '8':
        print(f"{num1} % {num2} = {mod(num1, num2)}")
    elif choice == '6':
        num = float(input("Enter number: "))
        try:
            print(f"Square root of {num} = {sqrt(num)}")
        except ValueError as e:
            print(e)
    elif choice == '7':
        num = int(input("Enter number: "))
        try:
            print(f"Factorial of {num} = {fact(num)}")
        except ValueError as e:
            print(e)
    elif choice == '9':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid input") 

print("Did you like to calculate more? (yes/no): ")
check = input("Yes or No: ")
check = "yes"

