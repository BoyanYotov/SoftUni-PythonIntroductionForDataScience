days = int(input())
total_consumption = 0

if days <= 0:
    print(0)
else:
    for day in range(1, days + 1):
        daily_consumption = int(input())
        total_consumption += daily_consumption
        print(total_consumption)
