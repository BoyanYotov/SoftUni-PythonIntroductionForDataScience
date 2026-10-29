n = int(input())
train = [0 for n in range(1, n + 1)]

while True:
    command = input()

    if command.startswith('add'):
        people = int(command.split()[1])
        train[-1] = train[-1] + people
    elif command.startswith('insert'):
        index = int(command.split()[1])
        people = int(command.split()[2])
        train[index] = train[index] + people
    elif command.startswith('leave'):
        index = int(command.split()[1])
        people = int(command.split()[2])
        train[index] = train[index] - people
    elif command == 'End':
        break

print(train)
