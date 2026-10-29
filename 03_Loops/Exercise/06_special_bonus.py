from math import ceil

stop_number = int(input())

while True:
    number = int(input())
    if number == stop_number:
        print(ceil(previous_number * 1.2))
        break
    previous_number = number
