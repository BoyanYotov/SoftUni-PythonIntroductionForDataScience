training_fee = int(input())

sneakers_price = training_fee * 0.6
team_price = sneakers_price * 0.8
ball_price = team_price * 0.25
accessories_price = ball_price * 0.2

total_amount = sneakers_price + team_price + ball_price + accessories_price + training_fee
print(total_amount)
