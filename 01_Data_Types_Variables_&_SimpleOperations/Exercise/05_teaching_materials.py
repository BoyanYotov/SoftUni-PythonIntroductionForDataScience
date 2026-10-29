PENS_PRICE = 5.80
MARKERS_PRICE = 7.20
BOARD_CLEANER_PER_LITER_PRICE = 1.2

pens_quantity = int(input())
marker_quantity = int(input())
board_cleaner_quantity = int(input())
discount = int(input())

total_amount_before_discount = ((pens_quantity * PENS_PRICE) + (marker_quantity * MARKERS_PRICE)
                                + (board_cleaner_quantity * BOARD_CLEANER_PER_LITER_PRICE))
discount = total_amount_before_discount * discount / 100

final_amount = total_amount_before_discount - discount

print(final_amount)
