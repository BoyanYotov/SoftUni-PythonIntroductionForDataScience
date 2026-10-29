tail = str(input())
body = str(input())
head = str(input())

animal = [tail, body, head]

animal[0], animal[2] = animal[2], animal[0]

print(animal)
