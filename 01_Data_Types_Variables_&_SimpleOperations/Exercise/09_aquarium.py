length = int(input())
width = int(input())
height = int(input())
percentage_decoration = float(input())

volume = length * width * height
liters = (volume - (volume * percentage_decoration / 100)) / 1000

print(f"{liters:.2f}")
