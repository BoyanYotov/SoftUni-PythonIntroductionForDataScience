number = int(input())


# def calculate_odd_and_even_sum(number):
#     sum_odd = 0
#     sum_even = 0
#
#     while number > 0:
#         last_digit = number % 10
#         if last_digit % 2 == 0:
#             sum_even += last_digit
#         else:
#             sum_odd += last_digit
#         number = number // 10
#     return f'Odd sum = {sum_odd}, Even sum = {sum_even}'
#
# print(calculate_odd_and_even_sum(number))

def calculate_even_odd_sum(number) -> str:
    sum_even = 0
    sum_odd = 0

    for digit in str(number):
        digit = int(digit)

        if digit % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit

    return f'Odd sum = {sum_odd}, Even sum = {sum_even}'


print(calculate_even_odd_sum(number))
