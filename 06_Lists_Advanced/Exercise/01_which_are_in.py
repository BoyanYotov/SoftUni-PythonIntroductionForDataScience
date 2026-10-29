list1 = input().split(', ')
list2 = input().split(', ')
filtered = []

for x in list1:
    for y in list2:
        if x in y:
            filtered.append(x)
            break

print(filtered)
