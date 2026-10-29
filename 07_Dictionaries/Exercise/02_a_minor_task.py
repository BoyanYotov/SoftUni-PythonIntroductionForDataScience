resources = {}

while True:
    resource = str(input())
    if resource == 'stop':
        break
    quantity = int(input())

    if resource not in resources:
        resources[resource] = quantity
    else:
        resources[resource] += quantity

for k, v in resources.items():
    print(f'{k} -> {v}')
