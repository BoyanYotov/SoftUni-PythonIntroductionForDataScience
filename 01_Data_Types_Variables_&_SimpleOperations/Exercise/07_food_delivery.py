CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DELIVERY = 2.50

chicken_menu_quantity = int(input())
fish_menu_quantity = int(input())
vegetarian_menu_quantity = int(input())

total_ordering = (chicken_menu_quantity * CHICKEN_MENU_PRICE) + (fish_menu_quantity * FISH_MENU_PRICE) + (
            vegetarian_menu_quantity * VEGETARIAN_MENU_PRICE)

dessert = total_ordering * 0.2

grand_total = total_ordering + dessert + DELIVERY
print(grand_total)
