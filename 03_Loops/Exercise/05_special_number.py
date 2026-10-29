initial_number = int(input())
n = initial_number
isSpecial = True

while n > 0:
    last_digit = n % 10
    if initial_number % last_digit == 0:
        n = n // 10
        continue
    else:
        print(f'{initial_number} is not special')
        isSpecial = False
        break

if isSpecial:
    print(f'{initial_number} is special')
