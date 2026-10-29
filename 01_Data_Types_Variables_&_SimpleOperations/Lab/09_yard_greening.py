PRICE_PER_SQUARE = 7.61
DISCOUNT_RATE = 0.18

square_meters = float(input())
discount = (square_meters * PRICE_PER_SQUARE) * DISCOUNT_RATE
total_cost = (square_meters * PRICE_PER_SQUARE) - discount

print(f'The final price is: {total_cost} lv.')
print(f'The discount is: {discount} lv.')
