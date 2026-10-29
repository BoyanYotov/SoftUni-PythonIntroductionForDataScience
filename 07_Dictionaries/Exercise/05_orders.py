products = {}

while True:
    command = input()
    if command == 'buy':
        break

    command = command.split()
    product = command[0]
    price = float(command[1])
    quantity = int(command[2])

    if product not in products:
        products[product] = []
        products[product].append(price)
        products[product].append(quantity)
    else:
        products[product][0] = price
        products[product][1] += quantity

for k, v in products.items():
    print(f"{k} -> {(v[0] * v[1]):.2f}")
