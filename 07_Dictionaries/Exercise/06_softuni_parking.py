n = int(input())
register = {}

for _ in range(n):
    command = input()
    if command.startswith('register'):
        command, name, number = command.split()
        if name not in register.keys():
            register[name] = number
            print(f'{name} registered {number} successfully')
        elif number in register.values():
            print(f'ERROR: already registered with plate number {number}')
    elif command.startswith('unregister'):
        command, name = command.split()
        if name not in register.keys():
            print(f'ERROR: user {name} not found')
        else:
            register.pop(name)
            print(f'{name} unregistered successfully')

for k, v in register.items():
    print(f'{k} => {v}')
