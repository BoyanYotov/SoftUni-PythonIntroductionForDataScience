phonebook = {}

while True:
    user_input = str(input())
    if '-' not in user_input:
        break
    name = str(user_input.split('-')[0])
    phone = str(user_input.split('-')[1])
    phonebook[name] = phone

n = int(user_input)
for i in range(n):
    name = str(input())
    if name in phonebook.keys():
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')
