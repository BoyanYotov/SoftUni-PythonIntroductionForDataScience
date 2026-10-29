number = int(input())
sum = 0
result = ""
for i in range(1, number + 1):
    sum += i
    if i < number:
        result += str(i)
        result += "+"
    else:
        result += str(i)
        result += "="
        result += str(sum)

print(result)
