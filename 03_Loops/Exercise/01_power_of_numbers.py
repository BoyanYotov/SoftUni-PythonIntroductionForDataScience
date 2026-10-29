a = int(input())
b = int(input())

current_sum = 0

for num in range(a, b + 1):
    current_sum = a ** num

print(current_sum)
