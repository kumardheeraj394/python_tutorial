import sys

def add(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):

    s = num1 - num2
    return s

def mul(num1, num2):
    m = num1 * num2
    return m

def div(num1, num2):
    d = num1 / num2
    return d

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "+":
    output = add(num1, num2)
elif operation == "-":
    output = sub(num1, num2)
elif operation == "*":
    output = mul(num1, num2)
elif operation == "/":
    output = div(num1, num2)
else:
    output = "Invalid operation"

print(output)    
