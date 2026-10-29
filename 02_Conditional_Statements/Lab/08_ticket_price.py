ticket_type = str(input())

if ticket_type == "student":
    ticket_price = 1.00
    print(f'${ticket_price:.2f}')
elif ticket_type == "regular":
    ticket_price = 1.60
    print(f'${ticket_price:.2f}')
else:
    print("Invalid ticket type!")
