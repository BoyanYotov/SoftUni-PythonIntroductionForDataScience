def calculate_total_price(product: str, quantity: int) -> float:
    if product == "coffee":
        price = 1.5
    elif product == "water":
        price = 1
    elif product == "coke":
        price = 1.4
    elif product == "snacks":
        price = 2
    return price * quantity


total_price = calculate_total_price(product=input(), quantity=int(input()))
print(f'{total_price:.2f}')
