numbers = list(map(int, input().split()))
opposite_numbers = []

for number in numbers:
    # if number < 0:
    #     opposite_numbers.append(abs(number))
    # else:
    #     opposite_numbers.append(-number)

    opposite_numbers.append(-number)

print(opposite_numbers)
