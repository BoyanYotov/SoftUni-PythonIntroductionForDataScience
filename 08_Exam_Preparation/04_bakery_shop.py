stock = {}
total_sold = 0

while True:
    user_input = input()
    if user_input == "Complete":
        break
    command, quantity, food = user_input.split(" ")
    quantity = int(quantity)
    if command == "Receive":
        if quantity <= 0:
            continue
        if food not in stock.keys():
            stock[food] = quantity
        else:
            stock[food] += quantity
    elif command == "Sell":
        if food not in stock.keys():
            print(f'You do not have any {food}.')
        else:
            if quantity <= stock[food]:
                stock[food] -= quantity
                total_sold += quantity
                print(f'You sold {quantity} {food}.')
                if stock[food] <= 0:
                    del stock[food]
            else:
                sold = stock[food]
                print(f'There aren\'t enough {food}. You sold the last {sold} of them.')
                total_sold += sold
                del stock[food]

for k, v in stock.items():
    print(f'{k}: {v}')
print(f'All sold: {total_sold} goods')
