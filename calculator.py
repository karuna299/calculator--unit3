def calculate(num1,num2,operator):
    if operator == "+":
       return num1 + num2
    elif operator == "*":
       return num1 * num2
    elif operator == "/":
       return num1 / num2
    elif operator == "-":
       return num1 - num2
    else:
        return "invalid operator"

