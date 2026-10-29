numbers = list(map(int, input().split(', ')))
beggars = int(input())

beggars_list = [0] * beggars

for i in range(0, len(numbers)):
    current_number = numbers[i]
    beggar_index = i % beggars
    beggars_list[beggar_index] += current_number

print(beggars_list)
