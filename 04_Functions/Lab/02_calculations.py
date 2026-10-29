# operator = str(input())
# number1 = int(input())
# number2 = int(input())
#
# def calculate(operator: str, number1: int, number2: int) -> int :
#     if operator == 'add':
#         return number1 + number2
#     elif operator == 'subtract':
#         return number1 - number2
#     elif operator == 'multiply':
#         return number1 * number2
#     elif operator == 'divide':
#         return number1 // number2
#
# print(calculate(operator, number1, number2))

operator = str(input())
number1 = int(input())
number2 = int(input())


def calculate(number1: int, number2: int, operator='multiply') -> int:
    if operator == 'add':
        return number1 + number2
    elif operator == 'subtract':
        return number1 - number2
    elif operator == 'multiply':
        return number1 * number2
    elif operator == 'divide':
        return number1 // number2


print(calculate(number1, number2, operator))
