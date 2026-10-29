NYLON_PRICE_PER_METER = 1.5
PAINT_PRICE_PER_LITER = 14.5
THINNER_PRICE_PER_LITER = 5

nylon_quantity = int(input())
paint_quantity = int(input())
thinner_quantity = int(input())
hours_work = int(input())

total_amount_materials = (((nylon_quantity + 2) * NYLON_PRICE_PER_METER) + (
            (paint_quantity * 1.1) * PAINT_PRICE_PER_LITER)
                          + (thinner_quantity * THINNER_PRICE_PER_LITER)) + 0.4
total_amount_work = total_amount_materials * 0.3 * hours_work

print(total_amount_work + total_amount_materials)
