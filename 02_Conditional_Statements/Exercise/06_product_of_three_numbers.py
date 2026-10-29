number1 = float(input())
number2 = float(input())
number3 = float(input())

if number1 == 0 or number2 == 0 or number3 == 0:
    print("zero")
else:
    negative_count = 0

    if number1 < 0:
        negative_count += 1
    if number2 < 0:
        negative_count += 1
    if number3 < 0:
        negative_count += 1

    if negative_count % 2 == 0:
        print("positive")
    else:
        print("negative")

# elif (number1 < 0 < number2 and number3 > 0) or (number1 > 0 > number2 and number3 > 0) or (
#         number1 > 0 > number3 and number2 > 0):
#     print("negative")
# elif (number1 < 0 and number2 < 0) or (number1 < 0 and number3 < 0) or (number2 < 0 and number3 < 0) :
#     print("positive")
