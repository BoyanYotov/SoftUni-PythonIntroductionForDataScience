temperature = int(input())
time_of_the_day = str(input())
clothing = None
shoes = None

if time_of_the_day == "Morning":
    if 10 <= temperature <= 18:
        clothing = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 <= temperature <= 24:
        clothing = "Shirt"
        shoes = "Moccasins"
    elif temperature >= 25:
        clothing = "T-Shirt"
        shoes = "Sandals"

elif time_of_the_day == "Afternoon":
    if 10 <= temperature <= 18:
        clothing = "Shirt"
        shoes = "Moccasins"
    elif 18 <= temperature <= 24:
        clothing = "T-Shirt"
        shoes = "Sandals"
    elif temperature >= 25:
        clothing = "Swim Suit"
        shoes = "Barefoot"

elif time_of_the_day == "Evening":
    if 10 <= temperature <= 18:
        clothing = "Shirt"
        shoes = "Moccasins"
    elif 18 <= temperature <= 24:
        clothing = "Shirt"
        shoes = "Moccasins"
    elif temperature >= 25:
        clothing = "Shirt"
        shoes = "Moccasins"

print(f"It's {temperature} degrees, get your {clothing} and {shoes}.")
