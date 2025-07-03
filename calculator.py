def multiply(a, b):
    return a * b 
  
def add(a, b):
    return a + b

def divide(a, b):
    return a / b

def subtract(a, b):
    return a - b

print("Ronak's Calculator")
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
operation = input("Choose (*, +, /, -): ")

if operation == "*":
    print("Result:", multiply(a, b))
elif operation == "+":
    print("Result:", add(a, b))
elif operation == "/":
    print("Result:", divide(a, b))
elif operation == "-":
    print("Result:", subtract(a, b))
else:
    print("Invalid operation.")
