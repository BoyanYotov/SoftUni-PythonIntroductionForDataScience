word = str(input())
chars = {}

for char in word:
    if char != ' ':
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

for k, v in chars.items():
    print(f'{k} -> {v}')
