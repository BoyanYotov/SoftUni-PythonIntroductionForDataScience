n = int(input())
synonyms = {}

for i in range(n):
    key = input()
    s = input()
    if key not in synonyms.keys():
        synonyms[key] = []
        synonyms[key].append(s)
    else:
        synonyms[key].append(s)

for k, w in synonyms.items():
    print(f'{k} - {", ".join(w)}')
