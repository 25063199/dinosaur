def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

print(calculate(10, 10, "+"))
print(calculate(10, 10, "-"))  
print(calculate(10, 10, "*")) 
print(calculate(10, 10, "/"))  