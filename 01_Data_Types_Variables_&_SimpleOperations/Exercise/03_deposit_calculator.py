deposited_amount = float(input())
months = int(input())
interest_rate = float(input())

total_amount = deposited_amount + (((deposited_amount * interest_rate / 100) / 12) * months)
print(total_amount)
