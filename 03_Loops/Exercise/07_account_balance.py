balance = 0

while True:
    command = input()
    if command == 'End':
        break

    amount = float(command)
    if amount <= 0:
        print(f'Decrease: {abs(amount):.2f}')
    else:
        print(f'Increase: {amount:.2f}')
    balance += amount

print(f'Balance: {float(balance):.2f}')
