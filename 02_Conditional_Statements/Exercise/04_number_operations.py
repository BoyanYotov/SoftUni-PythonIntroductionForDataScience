number1 = int(input())
number2 = int(input())
operator = str(input())
result = None

if operator == "+":
    result = number2 + number1
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2

print(f'{number1} {operator} {number2} = {result:.2f}')
