num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
operator=input("Enter operator (+, -, *, /): ")

if operator == '+':
    result = num1+num2
elif operator == '-':
    result = num1-num2
elif operator == '*':
    result = num1*num2
elif operator == '/':
    if num2 !=0:
        result = num1/num2
    else: 
        result = "Error! Division by zero."
else:
    result = "Error! Invalid operator."
print("Result:", result)
# This is a simple calculator that performs basic arithmetic operations