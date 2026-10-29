season = str(input())
accommodation = str(input())
days = int(input())

price_per_night = None
discount = None

if season == "Spring":
    discount = 0.8
    if accommodation == "Hotel":
        price_per_night = 30
    elif accommodation == "Camping":
        price_per_night = 10

elif season == "Summer":
    discount = 1
    if accommodation == "Hotel":
        price_per_night = 50
    elif accommodation == "Camping":
        price_per_night = 30

elif season == "Autumn":
    discount = 0.7
    if accommodation == "Hotel":
        price_per_night = 20
    elif accommodation == "Camping":
        price_per_night = 15

elif season == "Winter":
    discount = 0.9
    if accommodation == "Hotel":
        price_per_night = 40
    elif accommodation == "Camping":
        price_per_night = 10

total_price = price_per_night * days * discount
print(f'{total_price:.2f}')
