numbers = list(map(int, input().split(', ')))
max_number = max(numbers)

for groups in range(10, max_number + 10, 10):
    current = [n for n in numbers if groups >= n > groups - 10]

    print(f'Group of {groups}\'s: {current}')
