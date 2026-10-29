numbers = list(map(int, input().split(', ')))
found_numbers = list(map(lambda x: x if numbers[x] % 2 == 0 else '', range(len(numbers))))
print(list(filter(lambda x: x != '', found_numbers)))
