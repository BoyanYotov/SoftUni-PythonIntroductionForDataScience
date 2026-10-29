from math import ceil, floor

paint_quantity = int(input())
wallpaper_quantity = int(input())
gloves_price = float(input())
brush_price = float(input())

paint_price = 21.50
wall_price = 5.20
gloves_quantity = ceil(wallpaper_quantity * 0.35)
brushes_quantity = floor(paint_quantity * 0.48)

total_amount = (paint_quantity * paint_price) + (gloves_quantity * gloves_price) + (brushes_quantity * brush_price) + (
            wallpaper_quantity * wall_price)
delivery = total_amount * 1 / 15

print(f'This delivery will cost {delivery:.2f} lv.')
