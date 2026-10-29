cpu_price = float(input())
video_card_price = float(input())
ram_price = float(input())
ram_count = int(input())
percent_discount = float(input())

total_price = ((cpu_price * (1 - percent_discount)) + (video_card_price * (1 - percent_discount)) + (
            ram_price * ram_count)) * 1.57
print(f'Money needed - {total_price:.2f} leva.')
