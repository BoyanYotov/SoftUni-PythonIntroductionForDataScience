current_version = list(map(int, input().split('.')))

current_version[-1] += 1

for i in range(2, 0, -1):
    if current_version[i] > 9:
        current_version[i] = 0
        current_version[i - 1] += 1

print(".".join(map(str, current_version)))
