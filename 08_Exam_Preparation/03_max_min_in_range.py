numbers = list(map(int, input().split()))
start = int(input())
end = int(input())

short_list = numbers[start:end + 1]
max = max(short_list)
min = min(short_list)

print(max + min)
