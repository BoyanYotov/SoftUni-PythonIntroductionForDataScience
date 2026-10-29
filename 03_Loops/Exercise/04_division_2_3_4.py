n = int(input())
divisible_by_two = 0
divisible_by_three = 0
divisible_by_four = 0

for i in range(1, n + 1):
    number = int(input())
    if number % 2 == 0:
        divisible_by_two += 1
    if number % 3 == 0:
        divisible_by_three += 1
    if number % 4 == 0:
        divisible_by_four += 1

print(f'{(divisible_by_two / n * 100):.2f}%')
print(f'{(divisible_by_three / n * 100):.2f}%')
print(f'{(divisible_by_four / n * 100):.2f}%')
