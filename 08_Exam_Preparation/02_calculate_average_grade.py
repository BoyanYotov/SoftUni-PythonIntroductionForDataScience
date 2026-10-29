n = int(input())

total = 0
for i in range(n):
    grade = float(input())
    total += grade
print(f'{total / n:.2f}')
