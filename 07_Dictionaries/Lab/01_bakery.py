elements = list(input().split())
foods = {}

while len(elements) > 0:
    key = elements.pop(0)
    val = int(elements.pop(0))
    foods[key] = val

print(foods)
