DOG_FOOD_PRICE = 2.5
CAT_FOOD_PRICE = 4

dog_food_packages = int(input())
cat_food_packages = int(input())

total_cost = (dog_food_packages * DOG_FOOD_PRICE) + (cat_food_packages * CAT_FOOD_PRICE)

print(f'{total_cost} lv.')
