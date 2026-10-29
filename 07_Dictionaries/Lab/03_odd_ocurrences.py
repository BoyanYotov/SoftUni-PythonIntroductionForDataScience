elements = list(input().split())
words = {}

for e in elements:
    e = e.lower()
    if e not in words.keys():
        words[e] = 1
    else:
        words[e] += 1

for key in words.keys():
    if words[key] % 2 != 0:
        print(key, end=" ")
